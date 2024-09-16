# GitHub Repository Sync Script

## Overview

This Python script automates the process of cloning and updating GitHub repositories from a specified organization. It uses asynchronous programming to efficiently process multiple repositories concurrently, ensuring that repositories are cloned if they don't exist locally or updated if they do.

## Features

- **Asynchronous Operations:** Uses Python's `asyncio` to handle concurrent repository processing.
- **Repository Management:** Clones new repositories and pulls updates for existing ones.
- **Progress Reporting:** Utilizes a custom progress bar with `tqdm` to display real-time progress.
- **Logging:** Captures detailed logs of the operations for debugging and review.
- **Result Summary:** Prints a summary of cloned, updated, and failed repository operations.

## Prerequisites

- **Python 3.10 or higher:** The script uses modern type annotations (e.g., union types with `|`).
- **GitHub CLI (gh):** This must be installed and configured to interact with GitHub repositories.
- **Git:** Required for cloning and updating repositories.
- Create a file called `.env` in the project root directory with the following information:
  ```conf
  ORG_NAME = 'your_org_name'
  REPO_PREFIX = 'your_repo_prefix'
  MAX_CONCURRENT_TASKS = 'your_max_concurrent_tasks'
  ```

## Setup

- `python3 -m venv .venv && source .venv/bin/activate` to create and activate a virtual environment
- `pip3 install -r requirements.txt` to install dependencies
- `python3 clone_or_pull_repos.py` to run the program