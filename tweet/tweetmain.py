import json
import tweepy

with open('secret.json') as f:
    twitter_keys = json.load(f)

# print(twitter_keys)

consumer_key = twitter_keys["consumer_key"]
consumer_secret = twitter_keys["consumer_secret"]
access_token = twitter_keys["access_token"]
access_token_secret = twitter_keys["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# print(api)

public_tweets = api.home_timeline()
print(public_tweets)