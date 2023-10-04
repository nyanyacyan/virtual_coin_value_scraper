from selenium import webdriver

url = "https://stepn-market.guide/market/dashboard"

driver = webdriver.Chrome(executable_path=)  # 修正必要

# URLを開く
driver.get(url)

# <b>タグのテキストを取得
all_btag_list = [b_tag.text for b_tag in driver.find_elements_by_tag_name('b')]
print(all_btag_list)

# 数字のみ、GMTは消去。
def string_intcleaning(s):
    cleaned = s.replace(" ","" ).replace("GMT", "")
    return int(cleaned)

# それぞれの範囲から抽出
sneaker_data = [string_intcleaning(value) for value in all_btag_list[:15]]
sneaker_count_data = [string_intcleaning(value) for value in all_btag_list[16:31]]
gems_data = [string_intcleaning(value) for value in all_btag_list[32:77]]
gems_count_data = [string_intcleaning(value) for value in all_btag_list[78:123]]
scroll_data = [string_intcleaning(value) for value in all_btag_list[124]]        # 修正必要
scroll_count_data = [string_intcleaning(value) for value in all_btag_list[125]]  # 修正必要

print(sneaker_data)
print(sneaker_count_data)
print(gems_data)
print(gems_count_data)
print(scroll_data)
print(scroll_count_data)