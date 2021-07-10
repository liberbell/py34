import json
import requests
import pandas as pd

URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

with open('key.txt') as f:
    API_key = f.readline()

params = {
    'key': API_key,
    'keyword': '神戸',
    'format': 'json',
    'count': 20,
}

res = requests.get(URL, params)
print(res.text)
print(res.json())
res = res.json()
print(res['results']['shop'])


print(json.dumps(res, indent=2, ensure_ascii=False))

items = res['results']['shop']
print(len(items))

df = pd.DataFrame(items)
print(df.columns)