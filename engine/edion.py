import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
import random
from common.logger import set_logger
import pandas as pd
import re
import time
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from common.operation_csv import *
logger = set_logger(__name__)

def fetch_edion_data(jan_list):
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)" \
        "AppleWebKit/537.36 (KHTML, like Gecko)" \
        "Chrome/96.0.4664.45"
    edion_item_data = []
    for jan in jan_list:
        print(jan)
        # 商品ページへ遷移
        if jan != '0':
            try:
                edion_url = f'https://www.edion.com/item_list.html?keyword={jan}'
                res = requests.get(edion_url,headers={"User-Agent": ua})
                time.sleep(1)
                soup = BeautifulSoup(res.content, "html.parser")
                name = soup.select("p.item")[0].text
                price_elem = soup.select("p.price2")[0].text
                price = re.sub(r'\D', '', price_elem) 
                url = soup.select("p.item > a")[0].get('href')
                url = 'https://www.edion.com' + url
            except Exception as e:
                logger.info(e)
                name = 'None'
                price = 999999
                url = 'None'
        else:
            name = 'None'
            price = 999999
            url = 'None'
        edion_item_data.append([name,price,url])  
        
    return edion_item_data

if __name__ == "__main__":
    fetch_edion_data()




        