import asyncio
import os
import json
import logging
import io
import traceback
from asyncio import Semaphore
from collections import defaultdict
from tqdm import tqdm
from decouple import config


# Set up environment variables
ORG_NAME = str(config("ORG_NAME"))
REPO_PREFIX = str(config("REPO_PREFIX"))
MAX_CONCURRENT_TASKS = int(config("MAX_CONCURRENT_TASKS"))

if ORG_NAME is None:
    raise Exception("Please set the ORG_NAME variable")
if REPO_PREFIX is None:
    raise Exception("Please set the REPO_PREFIX variable")
if MAX_CONCURRENT_TASKS is None:
    raise Exception("Please set the MAX_CONCURRENT_TASKS variable")


# Set up logging
log_stream = io.StringIO()
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=log_stream,
)
logger = logging.getLogger(__name__)


# Global dictionary to store results
results = defaultdict(list)


class CustomProgressBar:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, total=None, desc=None):
        if not hasattr(self, "pbar"):
            self.pbar = tqdm(total=total, desc=desc, leave=True) if total else None
        self.last_update = 0

    def start(self, total, desc):
        self.pbar = tqdm(total=total, desc=desc, leave=True)
        self.last_update = 0

    def update(self, n=1):
        if self.pbar:
            self.pbar.update(n)
            self.last_update += n

    def write(self, s):
        logger.info(s)

    def close(self):
        if self.pbar:
            self.pbar.close()
        self.pbar = None


# Create a global instance of CustomProgressBar
progress_bar = CustomProgressBar()


async def run_command(
    cmd: str, repo_name: str, cwd=None
) -> tuple[int | None, str, str]:
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE, cwd=cwd
    )
    stdout, stderr = await process.communicate()
    if stderr and process.returncode != 0:
        logger.error(
            f"Error in '{repo_name}': Command '{cmd}' failed: {stderr.decode().strip()}"
        )
    elif stderr:
        logger.info(
            f"Info from '{repo_name}': Command '{cmd}' output: {stderr.decode().strip()}"
        )
    return process.returncode, stdout.decode(), stderr.decode()


async def get_repos(ORG_NAME: str) -> list[dict]:
    process = await asyncio.create_subprocess_shell(
        f"gh repo list {ORG_NAME} --json name --limit 1000",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    if process.returncode != 0:
        logger.error(f"Error fetching repos: {stderr.decode().strip()}")
        return []
    return json.loads(stdout)


async def clone_repo(repo_name: str, repo_path: str):
    returncode, _, stderr = await run_command(
        f"gh repo clone {ORG_NAME}/{repo_name} {repo_path}", repo_name
    )
    if returncode == 0:
        results["cloned"].append(repo_name)
    else:
        results["clone_failed"].append((repo_name, stderr.strip()))


async def get_commit_hash(repo_name: str, repo_path: str):
    returncode, commit_hash, _ = await run_command(
        "git rev-parse HEAD", repo_name, cwd=repo_path
    )
    return commit_hash.strip() if returncode == 0 else None


async def get_changed_files(
    repo_name: str, repo_path: str, before_commit: str | None, after_commit: str | None
):
    returncode, changed_files_output, _ = await run_command(
        f"git diff --name-only {before_commit} {after_commit}", repo_name, cwd=repo_path
    )
    return (
        changed_files_output.strip().split("\n") if changed_files_output.strip() else []
    )


async def update_repo(repo_name: str, repo_path: str):
    before_commit = await get_commit_hash(repo_name, repo_path)

    returncode, output, error = await run_command(
        "git pull --ff-only", repo_name, cwd=repo_path
    )
    if returncode != 0:
        results["update_failed"].append((repo_name, error.strip()))
        return

    after_commit = await get_commit_hash(repo_name, repo_path)

    if before_commit != after_commit:
        changed_files = await get_changed_files(
            repo_name, repo_path, before_commit, after_commit
        )
        if changed_files:
            results["updated"].append((repo_name, changed_files))
        else:
            results["updated_state"].append(repo_name)
    else:
        results["up_to_date"].append(repo_name)


async def clone_or_sync_repo(repo_name: str):
    repo_path = os.path.join(os.getcwd(), repo_name)

    if os.path.exists(repo_path):
        await update_repo(repo_name, repo_path)
    else:
        await clone_repo(repo_name, repo_path)


async def process_repos(repos):
    semaphore = Semaphore(MAX_CONCURRENT_TASKS)
    total_repos = len(repos)
    progress_bar.start(total=total_repos, desc="Processing repositories")

    async def process_with_semaphore(repo_name):
        async with semaphore:
            try:
                await asyncio.wait_for(clone_or_sync_repo(repo_name), timeout=60)
            except asyncio.TimeoutError:
                logger.error(f"Timeout processing repository: {repo_name}")
                results["update_failed"].append((repo_name, "Timeout"))
            except Exception as e:
                logger.error(f"Error processing repository {repo_name}: {str(e)}")
                results["update_failed"].append((repo_name, str(e)))
            finally:
                progress_bar.update(1)

    tasks = [process_with_semaphore(repo["name"]) for repo in repos]
    await asyncio.gather(*tasks)
    progress_bar.close()


def print_results():
    print("\n" + "=" * 50)
    print("Sync Results Summary")
    print("=" * 50)

    if results["cloned"]:
        print("\nCloned Repositories:")
        for repo in results["cloned"]:
            print(f"  - {repo}")

    if results["updated"]:
        print("\nUpdated Repositories:")
        for repo, files in results["updated"]:
            print(f"  - {repo}")
            for file in files:
                print(f"    * {file}")

    if results["updated_state"]:
        print("\nUpdated Repositories (State Only, No File Changes):")
        for repo in results["updated_state"]:
            print(f"  - {repo}")
        print(
            "  These repositories were updated (e.g., new merge commit) but no files were changed."
        )

    if results["up_to_date"]:
        print("\nAlready Up-to-Date Repositories:")
        for repo in results["up_to_date"]:
            print(f"  - {repo}")

    if results["update_failed"]:
        print("\nFailed Updates:")
        for repo, error in results["update_failed"]:
            print(f"  - {repo}: {error}")

    if results["clone_failed"]:
        print("\nFailed Clones:")
        for repo, error in results["clone_failed"]:
            print(f"  - {repo}: {error}")

    print("\n" + "=" * 50)
    print("Summary Counts")
    print("=" * 50)
    print(f"Cloned: {len(results['cloned'])}")
    print(f"Updated: {len(results['updated'])}")
    print(f"Updated (State Only): {len(results['updated_state'])}")
    print(f"Already Up-to-Date: {len(results['up_to_date'])}")
    print(f"Failed Updates: {len(results['update_failed'])}")
    print(f"Failed Clones: {len(results['clone_failed'])}")
    print("=" * 50)


async def main():
    try:
        all_repos = await get_repos(ORG_NAME)
        filtered_repos = [
            repo for repo in all_repos if repo["name"].startswith(REPO_PREFIX)
        ]
        print(
            f"Processing {len(filtered_repos)} '{REPO_PREFIX}' repositories out of {len(all_repos)} total repositories."
        )
        await process_repos(filtered_repos)
        print_results()

        # Print log contents
        log_contents = log_stream.getvalue().strip()
        if log_contents:
            print("\nLog contents:")
            print("=" * 50)
            print(log_contents)
        else:
            print("\nNo log messages were generated.")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        logger.error("Exception details:")
        logger.error(traceback.format_exc())


if __name__ == "__main__":
    asyncio.run(main())
