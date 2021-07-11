import json
import requests
import pandas as pd

URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'

with open('key.txt') as f:
    API_key = f.readline()

params = {
    'applicationId': API_key,
    'format': 'json',
    'keyword': 'タブレット',
    'maxPrice': 20000,
}

res = requests.get(URL, params)
# print(res.status_code)

res = res.json()
# print(json.dumps(res, indent=2, ensure_ascii=False))

items = res['Items']
# print(json.dumps(items, indent=2, ensure_ascii=False))
print(len(items))
print(json.dumps(items[0], indent=2, ensure_ascii=False))

# pd = pd.DataFrame(items)
# print(pd[:3])

items = [item['Item'] for item in items]
print(items[1])

df = pd.DataFrame(items)
print(df[:3])