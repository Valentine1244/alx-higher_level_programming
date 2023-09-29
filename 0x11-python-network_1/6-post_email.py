#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import requests
    import sys

    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
