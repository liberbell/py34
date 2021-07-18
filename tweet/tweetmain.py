import json
import tweepy
from tweepy.api import API
from tweepy.models import Status

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

# public_tweets = api.home_timeline()
# print(public_tweets)
# for tweet in public_tweets:
#     print(tweet.text)

me = api.me()
# print(me.followers_count)
# print(me.friends_count)
# print(me.followers)

# get_user01 = api.get_user("@yousuck2020")
# print(get_user01.followers_count)
# print(get_user01.entities)

api.update_status("This message is test from API.")
api.update_with_media(status="This message is test with file from API.", filename=sample.jpg)