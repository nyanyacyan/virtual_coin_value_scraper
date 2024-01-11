from selenium import webdriver  # seleniumのバージョンを4.1にする
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # Chromeのバージョンをオートで確認してくれてインストールしてくれる
import re
import pandas as pd
import csv

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
all_btag_list = [b_tag.text for b_tag in driver.find_elements(By.TAG_NAME, 'b')]

cleaned_list = [clean_and_convert(item) for item in all_btag_list]
with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for index, item in enumerate(cleaned_list, start=1):
        writer.writerow([index, item])

# それぞれの範囲から抽出
# 更新する際にはここを更新→スプシ「all_list」を確認必要。
Sneaker_data = cleaned_list[:16]
Sneaker_rainbow_data = cleaned_list[16]
print(Sneaker_rainbow_data)

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
all_tdtag_list = [td_tag.text for td_tag in driver.find_elements(By.TAG_NAME, 'td')]


Sneaker_None_data = [zero_replace(element) for element in all_tdtag_list[21:24]]
Sneaker_count_None_data = [zero_replace(element) for element in all_tdtag_list[46:49]]

Gems_lv6_Rainbow_None_data = zero_replace(all_tdtag_list[85])
Gems_lv7_Rainbow_None_data = zero_replace(all_tdtag_list[91])
Gems_lv8_Comfort_None_data = zero_replace(all_tdtag_list[95])
Gems_lv8_Rainbow_None_data = zero_replace(all_tdtag_list[97])
Gems_lv9_R_E_None_data = [zero_replace(element) for element in all_tdtag_list[99:102]]
Gems_lv9_Rainbow_None_data = zero_replace(all_tdtag_list[103])

Gems_count_lv7_Rainbow_None_data = zero_replace(all_tdtag_list[145])
Gems_count_lv8_Rainbow_None_data = zero_replace(all_tdtag_list[151])
Gems_count_lv9_Rainbow_None_data = zero_replace(all_tdtag_list[157])


# WebDriverを閉じる
driver.quit()