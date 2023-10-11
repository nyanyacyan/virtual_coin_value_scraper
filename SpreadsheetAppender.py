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
Gems_data_with_date = [current_date] + scraper.Gems_lv1_lv5_data
Gems_count_data_with_date = [current_date] + scraper.Gems_count_data
Scroll_data_with_date = [current_date] + scraper.Scroll_data
Scroll_count_data_with_date = [current_date] + scraper.Scroll_count_data


# sneaker_data   リストでの入力
def append_Sneaker_data():
    Sneaker_column_data = Sneaker_worksheet.col_values(1) # A列の最終行を見つける

    last_row = len(Sneaker_column_data)

    range_notation = f'A{last_row + 1}' # 空白のセルにデータを追加する範囲を指定

    # updateメソッドを使ってデータを書き込む
    append_Sneaker_data = Sneaker_worksheet.update(range_notation, [Sneaker_data_with_date])
    return append_Sneaker_data


# Sneaker_rainbow_data
# U列は21列目   セル単体での追加
def append_Sneaker_rainbow_data():
    Sneaker_U_column = Sneaker_worksheet.col_values(21)  # 21はU列
    last_row = len(Sneaker_U_column)

    append_Sneaker_rainbow_data = Sneaker_worksheet.update_cell(last_row + 1, 21, scraper.Sneaker_rainbow_data)
    return append_Sneaker_rainbow_data


# sneaker_count_data
def append_Sneaker_count_data():
    Sneaker_column_data = Sneaker_worksheet.col_values(23)  # W列の最終行を見つける

    last_row = len(Sneaker_column_data)


    range_notation = f'W{last_row + 1}'  # 空白のセルにデータを追加する範囲を指定

    append_Sneaker_count_data = Sneaker_worksheet.update(range_notation, [Sneaker_count_data_with_date])
    return append_Sneaker_count_data


# Sneaker_count_rainbow_data
# AQ列43
def append_Sneaker_count_rainbow_data():
    Sneaker_AQ_column = Sneaker_worksheet.col_values(43)  
    last_row = len(Sneaker_AQ_column)

    append_Sneaker_rainbow_data = Sneaker_worksheet.update_cell(last_row + 1, 43, scraper.Sneaker_rainbow_data)
    return append_Sneaker_rainbow_data


# gems_data
# gspreadは１から始まる
def append_gems_data():
    Gems_column_data = Gems_worksheet.col_values(1) # A列の最終行を見つける

    last_row = len(Gems_column_data)

    range_notation = f'A{last_row + 1}' # 空白のセルにデータを追加する範囲を指定

    # updateメソッドを使ってデータを書き込む
    append_Gems_data = Gems_worksheet.update(range_notation, [Gems_data_with_date])
    return append_Gems_data


# Gems_lv6_data
def append_gems_lv6_data():
    Gems_column_data = Gems_worksheet.col_values(27)

    last_row = len(Gems_column_data)
    print(last_row)

    range_notation = f'AA{last_row + 1}'

    # updateメソッドを使ってデータを書き込む
    append_Gems_lv6_data = Gems_worksheet.update(range_notation, [scraper.Gems_lv6_data])
    return append_Gems_lv6_data

# Gems_lv7_data
def append_gems_lv7_data():
    Gems_column_data = Gems_worksheet.col_values(31)

    last_row = len(Gems_column_data)
    print(last_row)

    range_notation = f'AF{last_row + 1}'

    # updateメソッドを使ってデータを書き込む
    append_Gems_lv7_data = Gems_worksheet.update(range_notation, [scraper.Gems_lv7_data])
    return append_Gems_lv7_data


# Gems_lv8_E_L_data
def append_gems_lv8_E_L_data():
    Gems_column_data = Gems_worksheet.col_values(37)

    last_row = len(Gems_column_data)
    print(last_row)

    range_notation = f'AK{last_row + 1}'

    # updateメソッドを使ってデータを書き込む
    append_Gems_lv8_E_L_data = Gems_worksheet.update(range_notation, [scraper.Gems_lv8_E_L_data])
    return append_Gems_lv8_E_L_data


# Gems_lv8_Resilience_data  単体
def append_gems_lv8_Resilience_data():
    Gems_AN_column = Gems_worksheet.col_values(40)
    last_row = len(Gems_AN_column)

    append_gems_lv8_Resilience_data = Gems_worksheet.update_cell(last_row + 1, 40, scraper.Gems_lv8_Resilience_data)
    return append_gems_lv8_Resilience_data


# Gems_lv9_Resilience_data  単体
def append_gems_lv9_Resilience_data():
    Gems_AS_column = Gems_worksheet.col_values(45)
    last_row = len(Gems_AS_column)

    append_gems_lv9_Resilience_data = Gems_worksheet.update_cell(last_row + 1, 45, scraper.Gems_lv9_Resilience_data)
    return append_gems_lv9_Resilience_data


# Gems_count_data
def append_Gems_count_data():
    Gems_column_data = Gems_worksheet.col_values(48)

    last_row = len(Gems_column_data)
    print(last_row)

    range_notation = f'AV{last_row + 1}'

    # updateメソッドを使ってデータを書き込む
    append_Gems_count_data = Gems_worksheet.update(range_notation, [Gems_count_data_with_date])
    return append_Gems_count_data


# Gems_count_lv7_data
def append_gems_lv7_data():
    Gems_column_data = Gems_worksheet.col_values(79)

    last_row = len(Gems_column_data)
    print(last_row)

    range_notation = f'CA{last_row + 1}'

    # updateメソッドを使ってデータを書き込む
    append_Gems_count_lv7_data = Gems_worksheet.update(range_notation, [scraper.Gems_count_lv7_data])
    return append_Gems_count_lv7_data


# Gems_count_lv8_data
def append_gems_lv8_data():
    Gems_column_data = Gems_worksheet.col_values(84)

    last_row = len(Gems_column_data)
    print(last_row)

    range_notation = f'CF{last_row + 1}'

    # updateメソッドを使ってデータを書き込む
    append_Gems_count_lv8_data = Gems_worksheet.update(range_notation, [scraper.Gems_count_lv8_data])
    return append_Gems_count_lv8_data


# Gems_count_lv9_data
def append_gems_lv9_data():
    Gems_column_data = Gems_worksheet.col_values(89)

    last_row = len(Gems_column_data)
    print(last_row)

    range_notation = f'CK{last_row + 1}'

    # updateメソッドを使ってデータを書き込む
    append_Gems_count_lv9_data = Gems_worksheet.update(range_notation, [scraper.Gems_count_lv9_data])
    return append_Gems_count_lv9_data


# Scroll_data
# gspreadは１から始まる
def append_Scroll_data():
    Scroll_column_data = Scroll_worksheet.col_values(1)

    last_row = len(Scroll_column_data)
    print(last_row)

    range_notation = f'A{last_row + 1}'

    # updateメソッドを使ってデータを書き込む
    append_Scroll_data = Scroll_worksheet.update(range_notation, [Scroll_data_with_date])
    return append_Scroll_data

# Scroll_count_data
def append_Scroll_count_data():
    Scroll_column_data = Scroll_worksheet.col_values(8)

    last_row = len(Scroll_column_data)
    print(last_row)

    range_notation = f'H{last_row + 1}'

    # updateメソッドを使ってデータを書き込む
    append_Scroll_count_data = Scroll_worksheet.update(range_notation, [Scroll_count_data_with_date])
    return append_Scroll_count_data

# 空白には０を入力