import gspread
from gspread_dataframe import set_with_dataframe
from gspread_formatting import *
from google.oauth2.service_account import Credentials
from gspread_formatting.batch_update_requests import format_cell_range

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'gcp_secret.json',
    scopes=scopes
)