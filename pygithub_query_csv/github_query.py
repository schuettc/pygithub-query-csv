import os
import csv
from github import Github

GITHUB_KEY = os.environ.get("POETRY_GITHUB_KEY")
g = Github(GITHUB_KEY)

with open("repos.csv", "w", newline="", encoding="utf-8") as csvfile:
    repo_writer = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    repo_writer.writerow(["Repo Name", "Repo Link", "Repo Pushed At", "Forks", "StarGazers", "Open Issues", "Security Alerts", "Open Pull Requests"])
    for repo in g.search_repositories(query="user:schuettc cdk"):
        repo_writer.writerow(
            [
                repo.name,
                repo.html_url,
                repo.pushed_at,
                repo.forks_count,
                repo.stargazers_count,
                repo.open_issues_count,
                repo.get_vulnerability_alert(),
                repo.get_pulls().totalCount,
            ]
        )
