import json

with open("plugins/secret.json") as f:
    slack_token = json.load(f)

API_TOKEN = slack_token["SLACK_TOKEN"]
# API_TOKEN = "abc"
DEFAULT_REPLY = "This is a default message."

PLUGINS = ["plugins"]