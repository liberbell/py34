import requests
import json

URL = "https://notify-api.line.me/api/notify"

with open("secret.txt") as f:
    line_token = json.load(f)

print(line_token)