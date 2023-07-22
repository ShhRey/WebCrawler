from selenium import webdriver                                                                      # Monitor Browser Activities
from selenium.webdriver.chrome.options import Options                                               # Keep Browser Open after Script Execution
from selenium.webdriver.common.by import By
import time
from db import *

options = Options()
options.add_experimental_option("detach", True)
path = "D:\\webdrivers\\chromedriver.exe" 
scrape_url = "https://coinmarketcap.com/exchanges/binance/"

driver = webdriver.Chrome(executable_path=path, options=options)
driver.get(scrape_url)
i=0
while True:
    try:
        button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div[2]/div/div[4]/div[3]/button')
        button.click()
        i += 1
        print("Button Pressed", i)
        time.sleep(10)
    except Exception as err:
        break

rows = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div[2]/div/div[4]/div[1]/div/table/tbody/tr')
coin_list = []

for row in rows:
    coin_data = {}
    coin_name = row.find_element(By.XPATH, './/td[2]/a')
    img_element = row.find_element(By.XPATH, './/td[2]/a/div/img')
    name = coin_name.get_attribute("href")
    img_url = img_element.get_attribute("src")
    coin_data['Name'] = name.split('https://coinmarketcap.com/currencies/')[1][:-1]
    coin_data['Image'] = img_url  
    coin_list.append(coin_data)


col2.insert_many(coin_list)