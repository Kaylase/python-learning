import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data["name"])
print(data["city"])
print(data["active"])
