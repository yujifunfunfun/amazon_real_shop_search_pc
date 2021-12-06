import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
import requests
from time import sleep
import pandas as pd
from common.logger import set_logger
logger = set_logger(__name__)


def fetch_yahoo_data(jan_list):
    yahoo_item_data = []
    for jan in jan_list:
        if jan != '0':
            try:
                url = f'https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch?appid=dj00aiZpPVdLMHFVS1dpTTMzVyZzPWNvbnN1bWVyc2VjcmV0Jng9MDQ-&jan_code={jan}&sort=%2Bprice&condition=new'
                r = requests.get(url)
                sleep(1)
                resp = r.json()
                item = resp['hits'][0]
                name = item['name']
                price = item['price']
                item_url = item['url']
            except Exception as e:
                logger.info(e)
                name = 'None'
                price = 999999
                item_url = 'None'
        else:
            name = 'None'
            price = 999999
            url = 'None'
        yahoo_item_data.append([name,price,item_url])
    
    return yahoo_item_data
            


if __name__ == "__main__":
    fetch_yahoo_data([4904810160373,4905330193568,769891491938])
