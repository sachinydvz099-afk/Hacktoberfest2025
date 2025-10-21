
import os
import sys
import subprocess

def run_cmd(cmd, cwd=None):
    try:
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {cmd}")
        print(e.stderr)
        sys.exit(1)

def clone_or_pull(repo_url, local_dir):
    if os.path.isdir(local_dir):
        print(f"Directory '{local_dir}' exists — pulling latest changes.")
        run_cmd(f"git -C {local_dir} pull")
    else:
        print(f"Cloning repository {repo_url} into '{local_dir}'.")
        run_cmd(f"git clone {repo_url} {local_dir}")

def list_branches(local_dir):
    print("Listing branches:")
    branches = run_cmd(f"git -C {local_dir} branch -a")
    print(branches)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 pull_github.py <repo-url> [<local-directory>]")
        sys.exit(1)

    repo_url = sys.argv[1]
    if len(sys.argv) >= 3:
        local_dir = sys.argv[2]
    else:
        local_dir = os.path.splitext(os.path.basename(repo_url.rstrip('/')))[0]

    clone_or_pull(repo_url, local_dir)
    list_branches(local_dir)

if __name__ == '__main__':
    main()
