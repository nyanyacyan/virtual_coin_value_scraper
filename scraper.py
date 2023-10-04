import requests
from selenium import webdriver

url = "https://stepn-market.guide/market/dashboard"
scraparsite = requests.get(url)

# 応答のステータスコードが200（成功）の場合、内容を表示
if scraparsite.status_code == 200:
    print(scraparsite.text)
else:
    print(f"Error {scraparsite.status_code}: Failed to fetch the webpage.")

sneaker_data = []
gems_data = []
scroll_data = []