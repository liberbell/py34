import gspread
from google.oauth2.service_account import Credentials


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'gcp_secret.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)
# print(gc)

SP_SHEET_KEY = '14240_Sv7TzeZVxBi42BtK6ZMtaRK82fYqvOqvR1js4s'
SP_SHEET = 'timesheet'

worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
worksheet