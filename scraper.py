from selenium import webdriver

url = "https://stepn-market.guide/market/dashboard"

driver = webdriver.Chrome(executable_path=)

# URLを開く
driver.get(url)

# <b>タグのテキストを取得
all_btag_list = [b_tag.text for b_tag in driver.find_elements_by_tag_name('b')]

# 数字のみ、GMTは消去。
def string_intcleaning(s):
    cleaned = s.replace(" ","" ).replace("GMT", "")
    return int(cleaned)

# それぞれの範囲から抽出
sneaker_data = [string_intcleaning(value) for value in all_btag_list[:4]]
gems_data = [string_intcleaning(value) for value in all_btag_list[:4]]
scroll_data = [string_intcleaning(value) for value in all_btag_list[:4]]

print(sneaker_data)
print(gems_data)
print(scroll_data)