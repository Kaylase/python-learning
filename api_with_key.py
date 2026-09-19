import os
from pathlib import Path
from dotenv import load_dotenv
import requests

env_path = Path(__file__).with_name(".env")
load_dotenv(env_path)

api_key = os.environ.get("MY_API_KEY")

if api_key is None:
    print("API key missing")
else:
    url = "https://httpbin.org/headers"

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, headers=headers, timeout=5)

    print("Status:", response.status_code)
    print(response.json())
