#!/usr/bin/python3
"""Takes a URL, sends a request and displays the X-Request-Id header value"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(
        url,
        headers={"cfclearance": "true"}
    )

    with urllib.request.urlopen(req) as response:
        request_id = response.getheader("X-Request-Id")
        print(request_id)
