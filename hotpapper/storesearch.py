import requests

URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

with open('key.txt') as f:
    API_key = f.readline()

params = {
    'key': API_key,
    'keyword': '神戸',
    'format': 'json'
}

res = requests.get(URL, params)
print(res.text)
print(res.json())
res = res.json()
print(res['results'])