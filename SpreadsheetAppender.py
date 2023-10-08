import gspread
from oauth2client.service_account import ServiceAccountCredentials
import scraper
import datetime

scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
service_account_file = 'gspread-401409-7403b643eb80.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(service_account_file, scopes)

gs = gspread.authorize(credentials)

spreadsheet_key = '1wGhuvB2Gs1btoq2DJlkdMlCixdvZdEazvYyOQm2T6EE'

# それぞれのワークシートを定義
Sneaker_worksheet = gs.open_by_key(spreadsheet_key).worksheet("Sneaker")
Gems_worksheet = gs.open_by_key(spreadsheet_key).worksheet("Gems")
Scroll_worksheet = gs.open_by_key(spreadsheet_key).worksheet("Scroll")


# 現在の日付を YYYY-MM-DD 形式で取得
current_date = datetime.datetime.now().strftime('%Y/%m/%d')

# 各データに日付をに追加して変数化
Sneaker_data_with_date = [current_date] + scraper.Sneaker_data
Sneaker_count_data_with_date = [current_date] + scraper.Sneaker_count_data
Gems_data_with_date = [current_date] + scraper.Gems_data
Gems_count_data_with_date = [current_date] + scraper.Gems_count_data
Scroll_data_with_date = [current_date] + scraper.Scroll_data
Scroll_count_data_with_date = [current_date] + scraper.Scroll_count_data

# sneaker_data
# gspreadは１から始まる
def append_Sneaker_data():
    Sneaker_column_data = Sneaker_worksheet.col_values(1)

    # Aの空白
    A_empty_row = len(Sneaker_column_data) + 1

    # 空白のセルにデータを追加
    range_to_write = f'A{A_empty_row}'
    append_Sneaker_data = Sneaker_worksheet.update(range_to_write, [Sneaker_data_with_date])
    return append_Sneaker_data

# sneaker_count_data
def append_Sneaker_count_data():
    Sneaker_column_data = Sneaker_worksheet.col_values(23)

    # Wの空白
    W_empty_row = len(Sneaker_column_data) + 1

    # 空白のセルにデータを追加
    range_to_write = f'W{W_empty_row}'
    append_Sneaker_count_data = Sneaker_worksheet.update(range_to_write, [Sneaker_count_data_with_date])
    return append_Sneaker_count_data


# gems_data
# gspreadは１から始まる
def append_gems_data():
    Gems_column_data = Gems_worksheet.col_values(1)

    # Aの空白
    A_empty_row = len(Gems_column_data) + 1

    # 空白のセルにデータを追加
    range_to_write = f'A{A_empty_row}'
    append_Gems_data = Gems_worksheet.update(range_to_write, [Gems_data_with_date])
    return append_Gems_data

# Gems_count_data
def append_Gems_count_data():
    Gems_column_data = Gems_worksheet.col_values(47)

    # Wの空白
    AV_empty_row = len(Gems_column_data) + 1

    # 空白のセルにデータを追加
    range_to_write = f'AV{AV_empty_row}'
    append_Gems_count_data = Gems_worksheet.update(range_to_write, [Gems_count_data_with_date])
    return append_Gems_count_data


# Scroll_data
# gspreadは１から始まる
def append_Scroll_data():
    Scroll_column_data = Scroll_worksheet.col_values(1)

    # Aの空白
    A_empty_row = len(Scroll_column_data) + 1

    # 空白のセルにデータを追加
    range_to_write = f'A{A_empty_row}'
    append_Scroll_data = Scroll_worksheet.update(range_to_write, [Scroll_data_with_date])
    return append_Scroll_data

# Scroll_count_data
def append_Scroll_count_data():
    Scroll_column_data = Scroll_worksheet.col_values(8)

    # Wの空白
    H_empty_row = len(Scroll_column_data) + 1

    # 空白のセルにデータを追加
    range_to_write = f'H{H_empty_row}'
    append_Scroll_count_data = Gems_worksheet.update(range_to_write, [Scroll_count_data_with_date])
    return append_Scroll_count_data