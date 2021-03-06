import gspread
from gspread_dataframe import set_with_dataframe
from gspread_formatting import *
from google.oauth2.service_account import Credentials
from gspread_formatting.batch_update_requests import format_cell_range
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
# set_with_dataframe(new_worksheet, pvt_table.reset_index(), row=first_row, col=first_col)

header_range = "B2:C2"
index_range = "B3:B8"
value_range = "C3:C8"

# header_fmt = CellFormat(
#     "backgroundColor": {
#         "red": 0.0,
#         "green": 0.0,
#         "blue": 0.0
#     },
#     "horizontalAlignment": "CENTER",
#     # textFormat = textFormat(bold=True, foregroundColor=color(255/255, 255/255, 255/255)),
#     "textFormat" : {
#         "foregroundColor" : {
#             "red": 1,
#             "green" : 1,
#             "blue" : 1
#         }
#         "bold" : True
#     }
# )
# header_fmt = CellFormat(
#     backgroundColor = color(38/255, 166/255, 154/255),
#     textFormat = textFormat(bold=True, foregroundColor=color(255/255, 255/255, 255/255)),
#     horizontalAlignment="CENTER"
# )

# format_cell_range(new_worksheet, header_range, header_fmt)
result_worksheet = sh.worksheet("new")

result_worksheet.format(header_range, {
    "backgroundColor": {
      "red": 38/255,
      "green": 166/255,
      "blue": 154/255
    },
    "horizontalAlignment": "CENTER",
    "textFormat": {
      "foregroundColor": {
        "red": 1.0,
        "green": 1.0,
        "blue": 1.0
      },
      "bold": True
    }
})

border_fmt = Border("DOTTED", Color(0, 0, 0, 0))
fmt = CellFormat(borders=Borders(top=border_fmt, left=border_fmt, right=border_fmt, bottom=border_fmt))
format_cell_range(result_worksheet, header_range, fmt)
format_cell_range(result_worksheet, index_range, fmt)
format_cell_range(result_worksheet, value_range, fmt)