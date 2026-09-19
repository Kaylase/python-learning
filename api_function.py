import os
from pathlib import Path

import requests
from dotenv import load_dotenv


def get_api_key():
    env_path = Path(__file__).with_name(".env")
    load_dotenv(env_path)

    api_key = os.environ.get("MY_API_KEY")

    if api_key is None:
        print("API key missing")
        return None

    return api_key


def get_data(api_key):
    url = "https://httpbin.invalid"

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=5
        )

        if response.status_code == 200:
            return response.json()
        else:
            print("HTTP error:", response.status_code)
            return None

    except requests.RequestException as error:
        print("Network error:", error)
        return None


api_key = get_api_key()

if api_key is not None:
    data = get_data(api_key)

    if data is not None:
        print(data)
