import gspread
from gspread_dataframe import set_with_dataframe
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
# print(df.shape)
df = df.drop(df.columns[[0]], axis=1)
# print(df.shape)
# print(df)

# print(df.pivot_table(index=["所属"], values=["年齢"], aggfunc='mean'))
# print(df.dtypes)
df = df.astype({"年齢": int, "社員ID": int})
# print(df.dtypes)
pvt_table = df.pivot_table(index=["所属"], values=["年齢"], aggfunc='mean')
print(pvt_table)

pvt_table["年齢"] = pvt_table["年齢"].round()

# new_worksheet = sh.add_worksheet(title="new", rows=100, cols=100)

first_row = 2
first_col = 2
# print(set_with_dataframe(new_worksheet, pvt_table.reset_index(), row=first_row, col=first_col))

header_range = "B2:C2"
index_range = "B3:B8"
value_range = "C3:C8"