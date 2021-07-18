import requests

with open('url.txt') as f:
    URL = f.readline()

res = requests.get(URL)
print(res.text)