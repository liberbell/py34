import requests

url = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

with open('key.txt') as f:
    key = f.readline()

print(key)