import pymongo

client = pymongo.MongoClient('mongodb://mongodbuser:wpytGAfnq%40%24%23P93Yt2y@mongo.profitsla.com:27017/?authMechanism=DEFAULT')
db = client['News-Data']

col1 = db['CoinGecko']