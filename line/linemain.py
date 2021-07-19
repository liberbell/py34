import requests
import json

# print(line_token)

def notify_message(message):
    URL = "https://notify-api.line.me/api/notify"

    with open("secret.txt") as f:
        line_token = json.load(f)

    LINE_NOTFY_TOKEN = line_token["LINE_NOTFY_TOKEN"]

    headers = {
        "Authorization": f'Bearer {LINE_NOTFY_TOKEN}'
    }

    data = {
        "message": message
    }

    requests.post(
        URL,
        headers=headers,
        data=data
    )

with open('secret.json') as f:
    twitter_keys = json.load(f)

consumer_key = twitter_keys["consumer_key"]
consumer_secret = twitter_keys["consumer_secret"]
access_token = twitter_keys["access_token"]
access_token_secret = twitter_keys["access_token_secret"]

message = "Message with function."
notify_message(message)