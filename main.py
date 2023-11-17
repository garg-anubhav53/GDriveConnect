import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe
from googleapiclient.discovery import build

def main(): 
    json_path = 'secondkey.json' # Please set the file for using service account.

    # try using oauth instead of service account

    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
    # client = gspread.authorize(creds)


    client = gspread.oauth(credentials_filename = 'oauthcred.json')
    spreadsheetTitle = 'Test Creation 10 From Python'
    folderId = '1Ck1IhgOIBsWs05xYGpQs9yYL9oUhkSc2' # Please set the folder ID of the folder in your Google Drive.

    original_spreadsheet = client.create(spreadsheetTitle, folder_id=folderId)
    original_workbook = original_spreadsheet.get_worksheet(0)

    original_workbook.append_row(["A single value", "A second single value"])

    print("Successfully created a new file and it can be accessed at ", original_workbook.url) 


if __name__ == '__main__': 
    main()