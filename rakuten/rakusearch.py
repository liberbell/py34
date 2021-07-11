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
print(res.status_code)