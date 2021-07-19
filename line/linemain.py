import requests
import json

URL = "https://notify-api.line.me/api/notify"

# print(line_token)

def notify_message(message):
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