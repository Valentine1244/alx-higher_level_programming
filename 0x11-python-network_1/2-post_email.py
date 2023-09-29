#!/usr/bin/python3
""" script that prints the value of the X-Request-Id
    variable found in the header of the response.
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8", "replace"))
