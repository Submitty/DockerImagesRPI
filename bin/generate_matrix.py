import json
import os
import subprocess
import sys
from pathlib import Path

if len(sys.argv) > 5:
    print("Too many arguments!", file=sys.stderr)
    exit(1)
elif len(sys.argv) < 3:
    print("Not enough arguments!", file=sys.argv)
    exit(1)

if not os.path.isdir("dockerfiles"):
    print("dockerfiles missing!", file=sys.stderr)
    exit(1)

username = sys.argv[1]
build_all = sys.argv[2]

to_build = []

if build_all == "false":
    hash_before = sys.argv[3]
    hash_after = sys.argv[4]

    # Get list of all changed files between 2 commits
    output = subprocess.check_output(["git", "--no-pager", "diff", "--name-only", hash_before, hash_after])
    paths_updated = output.decode("utf-8").splitlines()

    for path in paths_updated:
        parts = Path(path).parts
        # Only rebuild if modified files were in dockerfiles
        if parts[0] != "dockerfiles":
            continue

        metadata = json.loads(open(Path(parts[0]) / parts[1] / "metadata.json").read())

        push_latest = False

        if metadata["pushLatest"]:
            if metadata["latestImage"] == parts[2]:
                push_latest = True

        tags = f"{username}/{parts[1]}:{parts[2]}"
        if push_latest:
            tags += f",{username}/{parts[1]}:latest"
        to_build.append(
            {
                "tags": tags,
                "context": str(os.path.dirname(path))
            }
        )
elif build_all == "true":
    images = os.listdir("dockerfiles")
    for image in images:
        path = Path("dockerfiles") / image
        if not path.is_dir():
            continue

        metadata = json.loads(open(path / "metadata.json").read())
        
        tags = os.listdir(path)
        for tag in tags:
            newpath = path / tag
            if not newpath.is_dir():
                continue
            
            push_latest = False
            if metadata["pushLatest"]:
                if metadata["latestImage"] == tag:
                    push_latest = True

            tags = f"{username}/{image}:{tag}"
            if push_latest:
                tags += f",{username}/{image}:latest"
            to_build.append(
                {
                    "tags": tags,
                    "context": str(newpath)
                }
            )


finobj = {"include": to_build}

print(json.dumps(finobj))
