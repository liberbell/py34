import requests
import json
import tweepy

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

def get_n_followers():
    consumer_key = twitter_keys["consumer_key"]
    consumer_secret = twitter_keys["consumer_secret"]
    access_token = twitter_keys["access_token"]
    access_token_secret = twitter_keys["access_token_secret"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    m = api.me()
    n_followers = m.followers_count
    return n_followers

message = f"Today's followers are {n_followers}."

notify_message(message)

