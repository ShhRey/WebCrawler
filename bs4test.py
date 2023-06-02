import requests, html5lib
from bs4 import BeautifulSoup

URL = "https://www.coingecko.com/en/news"
r = requests.get(url=URL)

all_news = []
soup = BeautifulSoup(r.content, 'html5lib') 
news_feed = soup.findAll('div', attrs={'data-target':'news.contentBox'})
for data in news_feed:
    print(data)
    news = {}
    news['title'] = data.article.div.div.img['alt']
    news['thumbnail'] = data.article.div.div.img['src']
    # news[''] = 
    # news[''] = 
    all_news.append(news)

print(all_news)