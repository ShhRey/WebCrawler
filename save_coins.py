import os, requests
from db import *

def download_save(url, name):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(name, "wb") as f:
            f.write(response.content)
            print(f"Image for {name} downloaded and saved")
    except Exception as err:
        print("Error Downloading Image", err)

folder_name = "Coins"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

dist_coins = col2.distinct('Name')
filtered_coins = [coin for coin in dist_coins if not any(substring in coin for substring in ["up", "down", "bear", "bull"])]
for coins in filtered_coins:
    c = col2.find_one({'Name': coins}, {'_id':0})
    cname = c['Name']
    curl = c['Image']
    fname = f"{cname}.png"
    fpath = os.path.join(folder_name, fname)
    download_save(url=curl, name=fpath)