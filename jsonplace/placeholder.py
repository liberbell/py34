import requests

url = 'https://jsonplaceholder.typicode.com/posts/'
res = requests.get(url)

print(res.text)