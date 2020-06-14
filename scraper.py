# A very basic Scraping Script where I keep track of Cyberpunk 2077's Price On Amazon !
import requests
from bs4 import BeautifulSoup

URL="https://www.amazon.in/CD-PROJEKT-RED-Cyberpunk-2077/dp/B07DWMND4R/ref=sr_1_13?dchild=1&keywords=cyberpunk+2077&qid=1590404230&sr=8-13"

headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}


page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = float(price.replace(',', ''))

print(converted_price)
print(title.strip())


