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
# print(df.columns)

colums = ['itemCode', 'itemName', 'itemPrice', 'catchcopy', 'availability', 'itemUrl', 'reviewAverage', 'reviewCount',
       'pointRateEndTime', 'shopName', 'creditCardFlag', 'genreId', 'itemUrl']

# print(df[colums])

new_colums = ['商品コード', '商品名', '商品価格', 'キャッチコピー', '在庫', '商品URL', 'レビュー平均', 'レビュー数',
       'ポイント終了日', 'テナント名', 'クレジットカード', '全般ID', '商品URL']

df.columns = new_colums
print(df[:3])