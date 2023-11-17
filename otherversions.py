# Below is some code that was tried to transfer ownership

# drive_scope = [ 'https://www.googleapis.com/auth/drive' ]

# # set variables from SO post 
# drive_credentials = creds
# spreadsheetId = ow_id

# drive_service = build('drive', 'v3', credentials=drive_credentials)

# # returns 'Permissions' dict
# permissions = drive_service.permissions().create(
#     fileId=spreadsheetId,
#     transferOwnership=True,
#     body={
#         'type': 'user',
#         'role': 'owner',
#         'emailAddress': 'garg.anubhav.xyz@gmail.com',
#     }
# ).execute()

# # apply permission 
# drive_service.files().update(
#     fileId=spreadsheetId,
#     body={'permissionIds': [permissions['id']]}
# ).execute()


# # original_workbook.share('garg.anubhav.xyz@gmail.com', perm_type='user', role='writer')



# # KEY = workbook.id # Please use your spreadsheet ID.
# # email = "garg.anubhav.xyz@gmail.com" # Please set email address you want to transfer the ownership.

# # ss_copy = client.copy(file_id=KEY)
# # res = ss_copy.share( email_address=email, perm_type="user", role="writer", notify=True)
# # permissionId = res.json()["id"]
# # ss_copy.transfer_ownership(permissionId)
# # print("This is the URL for the newly transferred sheet", ss_copy.url)

# # print ("This is what is stored after trying to open a spreadsheet ", sh)