import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random
from common.logger import set_logger
import pandas as pd
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from common.chromedriver import *

logger = set_logger(__name__)



def start_chrome():
    global option

    user_agent = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69"
    ]
    UA = user_agent[random.randrange(0, len(user_agent), 1)]
    option = Options()                         
    # option.add_argument('--headless') 
    option.add_argument('--lang=ja-JP')
    option.add_argument('--user-agent=' + UA)
    option.add_argument('--ignore-certificate-errors')
    option.add_argument('--ignore-ssl-errors')
    option.add_argument("window-size=1000,600")
    #ここで、バージョンなどのチェックをする
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)   

def fetch_laox_data(driver,model_number_list):
    wait = WebDriverWait(driver, 20)
    driver.get('https://www.laox-online.jp/info/')
    element = wait.until(EC.presence_of_all_elements_located)
    laox_item_data = []
    for model_number in model_number_list:
        print(model_number)
        # 商品ページへ遷移
        if model_number != 'None':
            try:
                driver.find_element_by_class_name('searchbox').clear()
                driver.find_element_by_class_name('searchbox').send_keys(model_number)
                driver.find_element_by_class_name('searchSubmit').click()
                element = wait.until(EC.presence_of_all_elements_located)
                name = driver.find_element_by_xpath('//*[@id="itemList"]/div/section/h2/a').text
                price = driver.find_element_by_class_name('selling_price').text
                price = re.sub(r'\D', '', price) 
                url = driver.find_element_by_xpath('//*[@id="itemList"]/div/section/h2/a').get_attribute('href')
            except Exception as e:
                logger.info(e)
                name = 'None'
                price = 999999
                url = 'None'
        else:
            name = 'None'
            price = 999999
            url = 'None'
        laox_item_data.append([name,price,url,''])
        

    return laox_item_data


if __name__ == "__main__":
    start_chrome()
    fetch_laox_data()