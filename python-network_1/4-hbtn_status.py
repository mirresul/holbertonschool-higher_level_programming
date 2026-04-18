#!/usr/bin/python3
"""Fetches a URL using requests and displays response info"""

import requests

if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")

    body = response.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
