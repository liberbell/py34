import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'secret.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)
print(gc)

SP_SHEET_KEY = '14240_Sv7TzeZVxBi42BtK6ZMtaRK82fYqvOqvR1js4s'
SP_SHEET = 'demo'

sh = gc.open_by_key(SP_SHEET_KEY)
# print(sh)

worksheet = sh.worksheet(SP_SHEET)
print(worksheet)
data = worksheet.get_all_values()
# print(data, end=", ")

df = pd.DataFrame(data[2:], columns=data[1])
print(df)