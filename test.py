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
sneaker_data_with_date = [current_date] + scraper.sneaker_data
sneaker_count_data_with_date = [current_date] + scraper.sneaker_count_data
gems_data_with_date = [current_date] + scraper.gems_data
gems_count_data_with_date = [current_date] + scraper.gems_count_data
scroll_data_with_date = [current_date] + scraper.scroll_data
scroll_count_data_with_date = [current_date] + scraper.scroll_count_data

# sneaker_data
# 最初の列（A）のデータを取得して最初の空白のセルを見つける
Sneaker_column_data = Sneaker_worksheet.col_values(1)
next_empty_row = len(Sneaker_column_data) + 1

# 空白のセルにデータを追加する
range_to_write = f'A{next_empty_row}:{chr(ord("A") + len(sneaker_data_with_date))}{next_empty_row}' # 後で意味を理解するのに確認必要
append_sneaker_data = Sneaker_worksheet.update(range_to_write, [sneaker_data_with_date])


# sneaker_count_data
# 最初の列（W）のデータを取得して最初の空白のセルを見つける
sneaker_count_column_data = Sneaker_worksheet.col_values(23)
next_empty_row = len(sneaker_count_column_data) + 1

# 空白のセルにデータを追加する
end_column = chr(ord("W") + len(sneaker_count_data_with_date[0]) - 1)
range_to_write = f'W{next_empty_row}:X{next_empty_row}' # 後で意味を理解するのに確認必要
print(range_to_write) 

append_sneaker_count_data = Sneaker_worksheet.update(range_to_write, [sneaker_count_data_with_date])
print(append_sneaker_count_data)