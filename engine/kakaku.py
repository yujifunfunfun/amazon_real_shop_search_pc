import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
import requests
from bs4 import BeautifulSoup
import re
from common.operation_csv import *
from common.logger import set_logger
logger = set_logger(__name__)


def fetch_kakaku_data(model_number_list):
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)" \
            "AppleWebKit/537.36 (KHTML, like Gecko)" \
            "Chrome/96.0.4664.45"

    kakaku_item_data = []
    for model_number in model_number_list:
        print(model_number)
        # 商品ページへ遷移
        if model_number != 'None':
            try:
                kakaku_url = f'https://kakaku.com/search_results/{model_number}/'
                res = requests.get(kakaku_url,headers={"User-Agent": ua})
                soup = BeautifulSoup(res.text, "html.parser")
                name = soup.select("p.p-item_name")[0].text
                price_elem = soup.select("p.p-item_price")[0].text
                price = re.sub(r'\D', '', price_elem) 
                url = soup.select("a.p-result_item_btn_link")[0].get('href')
            except Exception as e:
                logger.info(e)
                name = 'None'
                price = 999999
                url = 'None'
        else:
            name = 'None'
            price = 999999
            url = 'None'
        kakaku_item_data.append([name,price,url])        

    return kakaku_item_data

if __name__ == "__main__":
    model_number_list = load_model_number()
    
    fetch_kakaku_data(model_number_list)




        