#!/usr/bin/python3
""" script that prints the value of the X-Request-Id
    variable found in the header of the response.
"""
if __name__ == "__main__":
    import request
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
