import requests
import json

URL = "https://notify-api.line.me/api/notify"

with open("secret.txt") as f:
    line_token = json.load(f)

# print(line_token)

LINE_NOTFY_TOKEN = line_token["LINE_NOTFY_TOKEN"]

message = "This is a message from python."

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