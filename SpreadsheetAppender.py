import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import scraper

def sheet_append_list(sheet, data):
    sheet.append_row([datetime.datetime.now().strftime('%Y-%m-%d')] + data)

def result_in_spreadsheet(data):
    # クレデンシャルのセットアップ
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    creds = ServiceAccountCredentials.from_json_keyfile_name('path_to_credentials.json', scope)
    client = gspread.authorize(creds)

    # スプレッドシートを開く
    spreadsheet = client.open("1wGhuvB2Gs1btoq2DJlkdMlCixdvZdEazvYyOQm2T6EE")

    # それぞれのワークシートにデータを追加
    sheet_append_list(spreadsheet.worksheet("Sneaker"), scraper.sneaker_data)
    sheet_append_list(spreadsheet.worksheet("Gems"), scraper.gems_data)
    sheet_append_list(spreadsheet.worksheet("Scroll"), scraper.scroll_data)