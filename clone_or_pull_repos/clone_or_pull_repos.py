import asyncio
import os
import json
import logging
from asyncio import Semaphore
from collections import defaultdict
from tqdm import tqdm

# Configuration
ORG_NAME = os.getenv("GITHUB_ORG", "")
REPO_PREFIX = os.getenv("REPO_PREFIX", "")
MAX_CONCURRENT_TASKS = int(os.getenv("MAX_CONCURRENT_TASKS", 20))

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global dictionary to store results
results = defaultdict(list)


async def async_tqdm(iterable, total=None, **kwargs):
    pbar = tqdm(total=total, **kwargs)
    for item in iterable:
        yield item
        pbar.update(1)
    pbar.close()


async def fetch_repos(ORG_NAME: str) -> list[dict]:
    process = await asyncio.create_subprocess_shell(
        f"gh repo list {ORG_NAME} --json name,sshUrl --limit 1000",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    if process.returncode != 0:
        logging.error(f"Error fetching repos: {stderr.decode().strip()}")
        return []
    return json.loads(stdout)


async def run_command(cmd: str, cwd=None) -> tuple[int | None, str, str]:
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE, cwd=cwd
    )
    stdout, stderr = await process.communicate()
    return process.returncode, stdout.decode(), stderr.decode()


async def get_changed_files(repo_path: str) -> list[str]:
    returncode, stdout, _ = await run_command("git status --porcelain", cwd=repo_path)
    if returncode == 0:
        return [line.split()[-1] for line in stdout.splitlines() if line.strip()]
    return []


async def clone_or_sync_repo(repo: dict):
    repo_name = repo["name"]
    ssh_url = repo["sshUrl"]
    repo_path = os.path.join(os.getcwd(), repo_name)

    if os.path.exists(repo_path):
        returncode, _, stderr = await run_command("git fetch --all", cwd=repo_path)
        if returncode == 0:
            returncode, before_commit, _ = await run_command(
                "git rev-parse HEAD", cwd=repo_path
            )
            returncode, _, stderr = await run_command(
                "git merge --ff-only @{u}", cwd=repo_path
            )
            returncode, after_commit, _ = await run_command(
                "git rev-parse HEAD", cwd=repo_path
            )

            if before_commit.strip() != after_commit.strip():
                changed_files = await get_changed_files(repo_path)
                if changed_files:
                    results["updated"].append((repo_name, changed_files))
                else:
                    results["updated_state"].append(repo_name)
            else:
                results["up_to_date"].append(repo_name)
        else:
            results["update_failed"].append((repo_name, stderr.strip()))
    else:
        returncode, _, stderr = await run_command(
            f"gh repo clone {ssh_url} {repo_path}"
        )
        if returncode == 0:
            results["cloned"].append(repo_name)
        else:
            results["clone_failed"].append((repo_name, stderr.strip()))


async def process_repos(repos):
    semaphore = Semaphore(MAX_CONCURRENT_TASKS)
    total_repos = len(repos)

    async def process_with_semaphore(repo):
        async with semaphore:
            await clone_or_sync_repo(repo)

    tasks = [process_with_semaphore(repo) for repo in repos]
    for _ in tqdm(
        asyncio.as_completed(tasks), total=total_repos, desc="Processing repositories"
    ):
        await _


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
        all_repos = await fetch_repos(ORG_NAME)
        filtered_repos = [
            repo for repo in all_repos if repo["name"].startswith(REPO_PREFIX)
        ]
        print(
            f"Processing {len(filtered_repos)} '{REPO_PREFIX}' repositories out of {len(all_repos)} total repositories."
        )
        await process_repos(filtered_repos)
        print_results()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    asyncio.run(main())
