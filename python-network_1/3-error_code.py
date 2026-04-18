#!/usr/bin/python3
"""Fetch URL and handle HTTPError exceptions"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(
        url,
        headers={"cfclearance": "true"}
    )

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode("utf-8"))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
