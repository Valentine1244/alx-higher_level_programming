#!/usr/bin/python3
""" script that prints the value of the X-Request-Id
    variable found in the header of the response.
"""
if __name__ == "__main__":
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
