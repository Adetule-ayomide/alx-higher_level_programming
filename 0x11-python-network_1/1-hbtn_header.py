#!/usr/bin/python3
import urllib.request
import sys
""" a Python script that takes in a URL, sends a request to the URL and display
    the value of the X-Request-Id variable found in the header of the response.
"""

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    request_id = response.getheader('X-Request-Id')
    print(request_id)
