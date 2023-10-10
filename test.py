import gspread
from oauth2client.service_account import ServiceAccountCredentials
import scraper
import datetime
import pandas as pd

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
Gems_data_with_date = [current_date] + scraper.Gems_lv1_lv5_data
Gems_count_data_with_date = [current_date] + scraper.Gems_count_data
Scroll_data_with_date = [current_date] + scraper.Scroll_data
Scroll_count_data_with_date = [current_date] + scraper.Scroll_count_data

# U列は21列目
# U列の最終行を見つける
col_values = Sneaker_worksheet.col_values(21)  # 21はU列
last_row = len(col_values)

Sneaker_worksheet.update_cell(last_row + 1, 21, scraper.Sneaker_rainbow_data)