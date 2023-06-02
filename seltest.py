from selenium import webdriver                                                                      # Monitor Browser Activities
from selenium.webdriver.chrome.options import Options                                               # Keep Browser Open after Script Execution
from selenium.webdriver.common.by import By                                                         # Filter/Search Webpage Elements
import time, uuid

def idgen():
    return uuid.uuid4().hex[:8].upper()

options = Options()
options.add_experimental_option("detach", True)
path = "D:\\webdrivers\\chromedriver.exe"                                                           # WebDriver File Path
newsURL = "https://www.coingecko.com/en/news"                                                       # URL you want to Scrape
driver = webdriver.Chrome(executable_path=path, options=options)         
driver.get(url=newsURL)
i = 0
while True:
    try:
        button = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[4]/div/button')
        button.click()
        i += 1
        print("Button Pressed", i)
        time.sleep(15)  # Wait for the new content to load
    except Exception as e:
        break  # Exit the loop if the button is no longer available


articles = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div/div[3]/article')

article_list = []

for article in articles:
    article_data = {}
    article_title = article.find_element(By.XPATH, './div/div[2]/header/h2').text
    article_link = article.find_element(By.XPATH, './div/div[2]/header/h2/a').get_attribute('href')
    article_img = article.find_element(By.XPATH, './div/div[1]/img').get_attribute("src")
    article_author = article.find_element(By.XPATH, './div/div[2]/header/p').text
    article_content = article.find_element(By.XPATH, './div/div[2]/div').text

    article_data['ArticleID'] = idgen()
    article_data['Link'] = article_link
    article_data['Title'] = article_title
    article_data['Image'] = article_img
    article_data['Author'] = article_author
    article_data['Content'] = article_content
    article_list.append(article_data)

# Print the list of article data
for article in article_list:
    print(article)