import requests

url = 'https://jsonplaceholder.typicode.com/posts/'
res = requests.get(url)

# print(res.status_code)
# print(res.json()[:5])

datam = res.json()[0]
print(datam['title'])