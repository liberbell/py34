from os import times
import gspread
from google.oauth2.service_account import Credentials
from gspread.models import Worksheet
import pandas as pd
from datetime import datetime

def auth():
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    credentials = Credentials.from_service_account_file(
        'gcp_secret.json',
        scopes=scopes
    )

    gc = gspread.authorize(credentials)

    SP_SHEET_KEY = '14240_Sv7TzeZVxBi42BtK6ZMtaRK82fYqvOqvR1js4s'
    SP_SHEET = 'timesheet'

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

# worksheet = auth()

# df = pd.DataFrame(worksheet.get_all_records())
# # print(df)

# timestamp = datetime.now()
# date = timestamp.strftime('%Y/%m/%d')
# p_time = timestamp.strftime('%H:%M')

# df = df.append({'date': date, 'start time': p_time, 'out time': '00:00'}, ignore_index=True)
# # print(df)

# worksheet.update([df.columns.tolist()] + df.values.tolist())

# timestamp = datetime.now()
# o_time = timestamp.strftime("%H:%M")

# df.iloc[-1. 2] = o_time
# df.iloc[-1, 2] = o_time

# worksheet.update([df.columns.tolist()] + df.values.tolist())

def start_time():
    worksheet = auth()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    p_time = timestamp.strftime('%H:%M')
    df = df.append({'date': date, 'start time': p_time, 'out time': '00:00'}, ignore_index=True)

    worksheet.update([df.columns.tolist()] + df.values.tolist())

def out_time():
    worksheet = auth()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    o_time = timestamp.strftime("%H:%M")

    df.iloc[-1, 2] = o_time
    worksheet.update([df.columns.tolist()] + df.values.tolist())

auth()
start_time()
out_time()