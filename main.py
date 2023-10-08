import unittest
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from SpreadsheetAppender import append_from_A  # あなたのスクリプト名をyour_scriptに置き換えてください

class TestSpreadsheetFunctions(unittest.TestCase):
    def test_append_from_A(self):
        # クレデンシャルのセットアップ
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/coinlocker/Desktop/virtual_coin_value_scraper/gspread-401409-7403b643eb80.json', scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open_by_key("1wGhuvB2Gs1btoq2DJlkdMlCixdvZdEazvYyOQm2T6EE")  # スプレッドシートのIDを指定してください
        sheet = spreadsheet.worksheet("Sneaker")  # ワークシート名を指定してください
        data = [1, 2, 3, 4, 5]
        append_from_A(sheet, data)

        # アサーションを使用して期待される結果と実際の結果を比較します
        last_row_values = sheet.row_values(sheet.row_count - 1)  # 最後の行の値を取得する仮想コード
        expected_values = [datetime.datetime.now().strftime('%Y-%m-%d')] + data  # 仮に今日が2023-10-10であるとする
        self.assertEqual(last_row_values, expected_values)  # 期待される結果と実際の結果が一致することを確認します

if __name__ == '__main__':
    unittest.main()


