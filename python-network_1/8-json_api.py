#!/usr/bin/python3
"""Search API script using POST request and JSON handling"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    q = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {"q": q}

    response = requests.post(url, data=data)

    try:
        json_data = response.json()

        if not json_data:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))

    except ValueError:
        print("Not a valid JSON")
