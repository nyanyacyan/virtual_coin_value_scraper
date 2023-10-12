from selenium import webdriver  # seleniumのバージョンを4.1にする
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # Chromeのバージョンをオートで確認してくれてインストールしてくれる
import re
# import pandas as pd

url = "https://stepn-market.guide/market/dashboard"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

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


# それぞれの範囲から抽出
Sneaker_data = cleaned_list[:16]
Sneaker_rainbow_data = cleaned_list[16]

Sneaker_count_data = cleaned_list[17:33]
Sneaker_count_rainbow_data = cleaned_list[33]

Gems_lv1_lv5_data = cleaned_list[34:59]
Gems_lv6_data = cleaned_list[59:63]
Gems_lv7_data = cleaned_list[63:67]
Gems_lv8_E_L_data = cleaned_list[67:69]
Gems_lv8_Resilience_data = cleaned_list[69]
Gems_lv9_Resilience_data = cleaned_list[70]

Gems_count_data = cleaned_list[71:101]
Gems_count_lv7_data = cleaned_list[101:105]
Gems_count_lv8_data = cleaned_list[105:109]
Gems_count_lv9_data = cleaned_list[109:113]

Scroll_data = [cleaned_list[113], cleaned_list[115], cleaned_list[117], cleaned_list[119], cleaned_list[121]]
Scroll_count_data = [cleaned_list[114], cleaned_list[116], cleaned_list[118], cleaned_list[120], cleaned_list[122]]

def zero_replace(element):
    element = element.replace('-', '0')
    try:
        return int(element)
    except ValueError:
        print(f"数値ではないものが入力されてます:{element}の部分システム構築の修正が必要です。")
        return None

# すべての<td>要素を抽出
all_tdtag_list = [td_tag.text for td_tag in driver.find_elements_by_tag_name('td')]

# -を０に置換
tdtag_0_replace = [zero_replace(element) for element in all_tdtag_list]

Sneaker_None_data = tdtag_0_replace[21:24]
Sneaker_count_None_data = tdtag_0_replace[46:49]
print(Sneaker_None_data)
Gems_lv6_Rainbow_None_data = tdtag_0_replace[85]
Gems_lv7_Rainbow_None_data = tdtag_0_replace[91]
Gems_lv8_Comfort_None_data = tdtag_0_replace[95]
Gems_lv8_Rainbow_None_data = tdtag_0_replace[97]
Gems_lv9_R_E_None_data = tdtag_0_replace[99:102]
Gems_lv9_Rainbow_None_data = tdtag_0_replace[103]

Gems_count_lv7_Rainbow_None_data = tdtag_0_replace[145]
Gems_count_lv8_Rainbow_None_data = tdtag_0_replace[151]
Gems_count_lv9_Rainbow_None_data = tdtag_0_replace[157]


# df = pd.DataFrame(all_tdtag_list, columns=['Value'])

# # CSVファイルとして保存
# df.to_csv('output.csv', index=False)

# デバック用
# print (f'Sneaker_data:{Sneaker_data}')
# print (f'Sneaker_rainbow_data:{Sneaker_rainbow_data}')
# print (f'Sneaker_count_data:{Sneaker_count_data}')
# print (f'Sneaker_count_rainbow_data:{Sneaker_count_rainbow_data}')

print (f'Gems_lv1_lv5_data:{Gems_lv1_lv5_data}')
# print (f'Gems_lv6_data:{Gems_lv6_data}')
# print (f'Gems_lv7_data:{Gems_lv7_data}')
# print (f'Gems_lv8_E_L_data:{Gems_lv8_E_L_data}')
# print (f'Gems_lv8_Resilience_data:{Gems_lv8_Resilience_data}')
# print (f'Gems_lv9_Resilience_data:{Gems_lv9_Resilience_data}')

# print (f'Gems_count_data:{Gems_count_data}')
# print (f'Gems_count_lv7_data:{Gems_count_lv7_data}')
# print (f'Gems_count_lv8_data:{Gems_count_lv8_data}')
# print (f'Gems_count_lv9_data:{Gems_count_lv9_data}')

# print (f'Scroll_data:{Scroll_data}')
# print (f'Scroll_count_data:{Scroll_count_data}')

# WebDriverを閉じる
driver.quit()