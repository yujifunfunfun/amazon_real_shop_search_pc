import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
import requests
from time import sleep
import pandas as pd
from common.logger import set_logger
logger = set_logger(__name__)


def fetch_rakuten_data(jan_list):
    rakuten_item_data = []
    for jan in jan_list:
        if jan != '0':
            try:      
                url = f'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?applicationId=1071977349781880110&keyword={jan}&sort=%2BitemPrice&NGKeyword=%E4%B8%AD%E5%8F%A4'
                r = requests.get(url)
                sleep(1)
                resp = r.json()
                item = resp['Items'][0]['Item']
                name = item['itemName']
                price = item['itemPrice']
                item_url = item['itemUrl'] 
            except Exception as e:
                logger.info(e)
                name = 'None'
                price = 999999
                item_url = 'None'
        else:
            name = 'None'
            price = 999999
            url = 'None'                
        rakuten_item_data.append([name,price,item_url])
    
    return rakuten_item_data
        


if __name__ == "__main__":
    fetch_rakuten_data([4904810160373,4905330193568,769891491938])