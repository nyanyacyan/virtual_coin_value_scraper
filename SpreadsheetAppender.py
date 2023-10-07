import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import scraper

def get_spreadsheet(data):
    # クレデンシャルのセットアップ
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/coinlocker/Desktop/virtual_coin_value_scraper/lively-paratext-401220-2654fb6e4f1e.json', scope)
    client = gspread.authorize(creds)
    return client.open("1wGhuvB2Gs1btoq2DJlkdMlCixdvZdEazvYyOQm2T6EE")

# spreadsheetのAから追記していく
def append_from_A(sheet, data):
    sheet.append_row([datetime.datetime.now().strftime('%Y-%m-%d')] + data)

# spreadsheetのHから追記していく
def append_from_H(sheet, data):
    # H列の空でないセルの数を取得して、次の行を決定
    w_calum_start = len(sheet.col_values(7)) + 1  # 23はW列のインデックス
    
    # 日付とデータをW列から書き込む
    sheet.update_cell(w_calum_start, 7, datetime.datetime.now().strftime('%Y-%m-%d'))  # 7はH列
    for i, value in enumerate(data, start=1):
        sheet.update_cell(w_calum_start, 7 + i, value)

# spreadsheetのWから追記していく
def append_from_W(sheet, data):
    # W列の空でないセルの数を取得して、次の行を決定
    w_calum_start = len(sheet.col_values(23)) + 1  # 23はW列のインデックス
    
    # 日付とデータをW列から書き込む
    sheet.update_cell(w_calum_start, 23, datetime.datetime.now().strftime('%Y-%m-%d'))  # 23はW列
    for i, value in enumerate(data, start=1):
        sheet.update_cell(w_calum_start, 23 + i, value)

# spreadsheetのAVから追記していく
def append_from_AV(sheet, data):
    # W列の空でないセルの数を取得して、次の行を決定
    av_calum_start = len(sheet.col_values(74)) + 1  # 74はAV列のインデックス
    
    # 日付とデータをW列から書き込む
    sheet.update_cell(av_calum_start, 74, datetime.datetime.now().strftime('%Y-%m-%d'))  # 74はW列
    for i, value in enumerate(data, start=1):
        sheet.update_cell(av_calum_start, 74 + i, value)


# それぞれのワークシートにデータを追加
def result_in_spreadsheet():
    spreadsheet = get_spreadsheet()
    append_from_A(spreadsheet.worksheet("Sneaker"), scraper.sneaker_data)
    append_from_W(spreadsheet.worksheet("Sneaker"), scraper.sneaker_count_data)
    append_from_A(spreadsheet.worksheet("Gems"), scraper.gems_data)
    append_from_AV(spreadsheet.worksheet("Gems"), scraper.gems_count_data)
    append_from_A(spreadsheet.worksheet("Scroll"), scraper.scroll_data)
    append_from_H(spreadsheet.worksheet("Scroll"), scraper.scroll_count_data)