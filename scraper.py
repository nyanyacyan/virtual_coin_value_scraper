from selenium import webdriver  # seleniumのバージョンを4.1にする
from webdriver_manager.chrome import ChromeDriverManager  # Chromeのバージョンをオートで確認してくれてインストールしてくれる
import re
# import pandas as pd

url = "https://stepn-market.guide/market/dashboard"

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# URLを開く
driver.get(url)

def clean_and_convert(item):
    cleaned_item = re.sub(r'[^\d.]', '', item)
    cleaned_item = cleaned_item.replace(',', '')
    try:
        return float(cleaned_item)
    except ValueError:
        print(f'{item}を変換できません')
        return None

# <b>タグのテキストを取得
all_btag_list = [b_tag.text for b_tag in driver.find_elements_by_tag_name('b')]

cleaned_list = [clean_and_convert(item) for item in all_btag_list]
# print(cleaned_list)

# # cleaned_listの内容をpandasデータフレームに変換
# df = pd.DataFrame(cleaned_list, columns=['Value'])

# # データフレームをExcelファイルとして保存
# df.to_excel('cleaned_list.xlsx', index=False)

# それぞれの範囲から抽出
Sneaker_data = cleaned_list[:16]
Sneaker_count_data = cleaned_list[17:33]
Gems_data = cleaned_list[34:70]
Gems_count_data = cleaned_list[71:112]
Scroll_data = [cleaned_list[113], cleaned_list[115], cleaned_list[117], cleaned_list[119], cleaned_list[121]]
Scroll_count_data = [cleaned_list[114], cleaned_list[116], cleaned_list[118], cleaned_list[120], cleaned_list[122]]

# print (f'sneaker_data:{sneaker_data}')
# print (f'sneaker_count_data:{sneaker_count_data}')
# print (f'gems_data:{gems_data}')
# print (f'gems_count_data:{gems_count_data}')
# print (f'scroll_data:{scroll_data}')
# print (f'scroll_count_data:{scroll_count_data}')