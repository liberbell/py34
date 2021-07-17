import json

with open('secret.json') as f:
    twitter_keys = json.load(f)

print(twitter_keys)