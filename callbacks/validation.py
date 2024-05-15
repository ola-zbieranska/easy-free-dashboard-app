# import pandas as pd
# # import gspread
# # from oauth2client.service_account import ServiceAccountCredentials
# import io
# import base64
#
# def validate_data(df):
#     errors = []
#     if 'age' in df.columns:
#         if any(df['age'] <= 0):
#             errors.append("W kolumnie 'age' znajdują się liczby niedodatnie.")
#     return errors
#
# # def get_google_sheet_data(sheet_url):
# #     scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# #     creds = ServiceAccountCredentials.from_json_keyfile_name('path_to_your_credentials_file.json', scope)
# #     client = gspread.authorize(creds)
# #     sheet = client.open_by_url(sheet_url)
# #     worksheet = sheet.get_worksheet(0)
# #     data = worksheet.get_all_records()
# #     df = pd.DataFrame(data)
# #     return df
#
# def parse_upload(contents, filename):
#     content_type, content_string = contents.split(',')
#     decoded = base64.b64decode(content_string)
#     try:
#         if 'csv' in filename:
#             df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
#         elif 'xls' in filename:
#             df = pd.read_excel(io.BytesIO(decoded))
#         return df
#     except Exception as e:
#         print(e)
#         return None