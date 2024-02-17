import requests

try:
    r = requests.get('https://api.github.com/users/python')
except Exception:
    print('No internet connectivity.')
else:
    print(requests.get('https://api.github.com/users/python').text)