from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
import base64

# SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

subscribers = [
    "sehihide@uma3.be",
    "kl6ew009hw@sute.jp"
]

def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)

def main():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'secret2.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    sender = "liberbell@gmail.com"
    subject = "test mail"
    message_text = "This is test mail by gmail API."

    # for to in subscribers:
    for num in range(len(subscribers)):
        to = subscribers[num-1]
    # to = subscribers[0]

        message = create_message(sender, to, subject, message_text)
        send_message(service, "me", message)

if __name__ == '__main__':
    main()