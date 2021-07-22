import json

with open("secret.json") as f:
    slack_token = json.load(f)

# API_TOKEN = slack_token["SLACK_TOKEN"]
API_TOKEN = slack_token["SLACK_TOKEN"]
DEFAULT_REPLY = "This is a default message."

PLUGINS = ["plugins"]