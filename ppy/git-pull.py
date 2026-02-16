#!/usr/bin/env -S uv run --script

# /// script
# dependencies = ["nbgitpuller"]
# ///

import argparse
import logging
from pathlib import Path

from nbgitpuller.pull import GitPuller

COURSE = "PPY1 2026"
COURSE_SLUG = COURSE.lower().replace(" ", "-")
GIT_URL = f"https://gitlab.fjfi.cvut.cz/ksi/{COURSE_SLUG}.git"
REPO_DIR = str(Path(__file__).parent)
if not Path(REPO_DIR, ".git").exists():
    REPO_DIR = str(Path(REPO_DIR, COURSE_SLUG))


def main():
    logging.basicConfig(
        format="[%(asctime)s] %(levelname)s -- %(message)s", level=logging.INFO
    )

    parser = argparse.ArgumentParser(
        description=f"Synchronizes a git repository for {COURSE} with a local repository."
    )
    parser.add_argument(
        "--git-url",
        default=GIT_URL,
        help="URL of the repo to sync (default: %(default)s)",
    )
    parser.add_argument(
        "--branch",
        default=None,
        help="Branch of repo to sync (default: %(default)s)",
    )
    parser.add_argument(
        "--repo-dir",
        default=REPO_DIR,
        help="Path to clone repo under (default: %(default)s)",
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        default=False,
        help="Whether to backup existing REPO_DIR if it exists",
    )
    args = parser.parse_args()

    for line in GitPuller(
        args.git_url,
        args.repo_dir,
        branch=args.branch if args.branch else None,
        backup=args.backup if args.backup else False,
    ).pull():
        print(line)


if __name__ == "__main__":
    main()
