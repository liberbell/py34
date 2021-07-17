import json
import tweepy

with open('secret.json') as f:
    twitter_keys = json.load(f)

tweepy.OAuthHandler(consumer_key, onsumer_secret)