#!/usr/bin/python3
import urllib
import sys
""" a Python script that takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header of the response.
"""

if __name__ == "__main__":
    arg = sys.argv[1]
    req = urllib.request.Request(arg)
    with urllib.request.urlopen(req) as response:
        result = response.getheader('X-Request-Id')
        print(result)
