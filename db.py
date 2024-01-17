import pymongo

client = pymongo.MongoClient('mongodb://mongodbuser:')
db = client['News-Data']

col1 = db['CoinGecko']
col2 = db['CoinMarketCap']
