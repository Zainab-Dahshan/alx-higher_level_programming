#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository."""

import sys
import requests

def get_recent_commits(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    r = requests.get(url)
    if r.status_code == 200:
        commits = r.json()
        for i in range(min(10, len(commits))):
            print(f"{commits[i].get('sha')}: {commits[i].get('commit').get('author').get('name')}")
    else:
        print(f"Error: {r.status_code} - {r.text}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <owner> <repo>")
        sys.exit(1)

    owner = sys.argv[1]
    repo = sys.argv[2]
    get_recent_commits(owner, repo)
