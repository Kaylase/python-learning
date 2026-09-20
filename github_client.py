import os
import json
from pathlib import Path

import requests
from dotenv import load_dotenv


def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"

    params = {
        "per_page": 5
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=5
        )

        response.raise_for_status()

        return response.json()

    except requests.HTTPError as error:
        print("HTTP error:", error)
        return None

    except requests.RequestException as error:
        print("Network error:", error)
        return None


def filter_repos(repos, min_stars, language=None):
    filtered = []

    for repo in repos:
        if repo["stargazers_count"] > min_stars:
            if language is None:
                filtered.append(repo)
            elif repo["language"] == language:
                filtered.append(repo)

    return filtered


def simplify_repos(repos):
    simplified = []

    for repo in repos:
        item = {
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "language": repo["language"],
            "url": repo["html_url"]
        }

        simplified.append(item)

    return simplified


def save_repos(repos, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(repos, file, indent=4)


def load_config():
    env_path = Path(__file__).with_name(".env")
    load_dotenv(env_path)

    username = os.environ.get("GITHUB_USERNAME")
    language = os.environ.get("LANGUAGE")
    min_stars_text = os.environ.get("MIN_STARS", "0")

    if username is None:
        print("GITHUB_USERNAME missing")
        return None

    try:
        min_stars = int(min_stars_text)

    except ValueError:
        print("MIN_STARS must be a number")
        return None

    return {
        "username": username,
        "min_stars": min_stars,
        "language": language
    }


def main():
    config = load_config()

    if config is None:
        return

    repos = get_repos(config["username"])

    if repos is None:
        return

    filtered = filter_repos(
        repos,
        config["min_stars"],
        config["language"]
    )

    simplified = simplify_repos(filtered)

    save_repos(
        simplified,
        "filtered_repos.json"
    )

    for repo in simplified:
        print(
            repo["name"],
            "-",
            repo["stars"],
            "-",
            repo["language"]
        )

        # Git practice: second commit
        

if __name__ == "__main__":
    main()
