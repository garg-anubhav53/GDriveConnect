import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe

json_path = 'secondkey.json' # Please set the file for using service account.

scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
client = gspread.authorize(creds)

print("Gets to line 11")
print("This is what is in client: ", client)

spreadsheetTitle = 'Test Creation 2 From Python'
folderId = '1Ck1IhgOIBsWs05xYGpQs9yYL9oUhkSc2' # Please set the folder ID of the folder in your Google Drive.

workbook = client.create(spreadsheetTitle)
sh = client.open(spreadsheetTitle)

print ("This is what is stored after trying to open a spreadsheet ", sh)