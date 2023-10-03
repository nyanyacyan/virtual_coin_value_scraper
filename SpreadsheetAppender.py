import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def store_in_spreadsheet(data):
    # クレデンシャルのセットアップ
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    creds = ServiceAccountCredentials.from_json_keyfile_name('path_to_credentials.json', scope)
    client = gspread.authorize(creds)

    # スプレッドシートを開く
    sheet = client.open("1wGhuvB2Gs1btoq2DJlkdMlCixdvZdEazvYyOQm2T6EE").sheet1

    # 最後の行にデータを追加
    next_row = len(sheet.col_values(1)) + 1  # 1列目の長さを取得して次の行を決定
    sheet.append_row([datetime.datetime.now().strftime('%Y-%m-%d')] + data)

# スクレイピングのロジック（ここは適宜修正してください）
data_scraped = ["sample_data1", "sample_data2", "sample_data3"]
store_in_spreadsheet(data_scraped)
