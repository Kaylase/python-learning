import os
from pathlib import Path

import requests
from dotenv import load_dotenv


def load_api_key():
    env_path = Path(__file__).with_name(".env")
    load_dotenv(env_path)

    api_key = os.environ.get("MY_API_KEY")

    if api_key is None:
        print("API key missing")
        return None

    return api_key


def make_request(api_key):
    url = "https://httpbin.org/headers"

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
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


def main():
    api_key = load_api_key()

    if api_key is None:
        return

    data = make_request(api_key)

    if data is None:
        return

    print(data)


if __name__ == "__main__":
    main()
