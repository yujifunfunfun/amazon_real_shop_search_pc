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




def fetch_yamada_data(model_number_list):
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)" \
        "AppleWebKit/537.36 (KHTML, like Gecko)" \
        "Chrome/96.0.4664.45"
    yamada_item_data = []
    for model_number in model_number_list:
        print(model_number)
        # 商品ページへ遷移
        if model_number != 'None':
            try:
                model_number = urllib.parse.quote(model_number)
                yamada_url = f'https://www.yamada-denkiweb.com/search/{model_number}/?path=&searchbox=1'
                res = requests.get(yamada_url,headers={"User-Agent": ua})
                time.sleep(2)
                soup = BeautifulSoup(res.content, "html.parser")
                name = soup.select("p.item-name")[0].text
                price_elem = soup.select("p.subject-text")[0].text
                price = re.sub(r'\D', '', price_elem) 
                url = soup.select("p.item-name > a")[0].get('href')
            except Exception as e:
                logger.info(e)
                name = 'None'
                price = 999999
                url = 'None'
        else:
            name = 'None'
            price = 999999
            url = 'None'
        yamada_item_data.append([name,price,url])  
        
    return yamada_item_data


if __name__ == "__main__":
    model_number_list = load_item_name()
    fetch_yamada_data(model_number_list)