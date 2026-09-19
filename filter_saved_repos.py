import os

api_key = os.environ.get("MY_API_KEY")

if api_key is not None:
    print("API key found")
else:
    print("API key missing")
