import requests
import os

def fetch_commits(repo):
    url = f"https://api.github.com/repos/{repo}/commits"
    response = requests.get(url)
    
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:  # Limit to 10 commits
            message = commit['commit']['message']
            author = commit['commit']['author']['name']
            print(f"Author: {author}\nMessage: {message}\n")
    else:
        print(f"Error fetching commits: {response.status_code}")

if __name__ == "__main__":
    repo = os.getenv("GITHUB_REPO", "torvalds/linux")  # Default repo if not set
    fetch_commits(repo)
