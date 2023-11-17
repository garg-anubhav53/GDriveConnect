import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe

json_path = 'uploadspreadsheet-405418-855ecfddad36.json' # Please set the file for using service account.

scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
client = gspread.authorize(creds)

spreadsheetTitle = 'Test Creation From Python'
folderId = '1Ck1IhgOIBsWs05xYGpQs9yYL9oUhkSc2' # Please set the folder ID of the folder in your Google Drive.

workbook = client.create(spreadsheetTitle, folder_id=folderId)