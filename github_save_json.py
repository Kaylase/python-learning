import requests
import json


def get_repos():
    url = "https://api.github.com/users/octocat/repos?per_page=5"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return response.json()

        else:
            print("HTTP error:", response.status_code)
            return None

    except requests.RequestException as error:
        print("Network error:", error)
        return None


repos = get_repos()

if repos is not None:
    with open("repos.json", "w") as file:
        json.dump(repos, file)

    print("Repos saved:", len(repos))

else:
    print("No repos to save")

    import json

with open("repos.json", "r") as file:
    repos = json.load(file)

print("Loaded repos:", len(repos))

for repo in repos:
    print(repo["name"])
