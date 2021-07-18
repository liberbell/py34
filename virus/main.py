import requests

with open('url.txt') as f:
    URL = f.readline()

res = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'})
print(res.text)