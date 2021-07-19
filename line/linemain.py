import requests
import json

# print(line_token)

def notify_message(message):
    URL = "https://notify-api.line.me/api/notify"
    
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