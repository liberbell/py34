import requests
import json


with open("secret.json") as f:
    slack_token = json.load(f)