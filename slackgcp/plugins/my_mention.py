from slackbot.bot import respond_to

import gspread
from google.oauth2.service_account import Credentials

import pandas as pd
from datetime import datetime

def auth():
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    credentials = Credentials.from_service_account_file(
        'plugins/gcp_secret.json',
        scopes=scopes
    )

    gc = gspread.authorize(credentials)

    SP_SHEET_KEY = '14240_Sv7TzeZVxBi42BtK6ZMtaRK82fYqvOqvR1js4s'
    SP_SHEET = 'timesheet'

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

@respond_to("work start")
def start_time(message):
    worksheet = auth()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    p_time = timestamp.strftime('%H:%M')
    message.send(f"Start time is {p_time}. Work hard.")
    df = df.append({'date': date, 'start time': p_time, 'out time': '00:00'}, ignore_index=True)

    worksheet.update([df.columns.tolist()] + df.values.tolist())
    print("start time regist done.")
    message.send("Start time is registerd. Work hard!!!")

@respond_to("beer")
def out_time(message):
    worksheet = auth()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    o_time = timestamp.strftime("%H:%M")
    message.send(f"out time is {o_time}. Really?")

    df.iloc[-1, 2] = o_time
    worksheet.update([df.columns.tolist()] + df.values.tolist())
    print("out time regist done.")
    message.send("Out time is registerd. Get out here.")