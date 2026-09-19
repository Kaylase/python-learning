repos = get_repos()

if repos is not None:
    for repo in repos:
        print(repo["name"])
else:
    print("API error")
