import json

with open("secret.json") as f:
    slack_token = json.load(f)

SLACK_TOKEN = slack_token["SLACK_TOKEN"]

print(SLACK_TOKEN)