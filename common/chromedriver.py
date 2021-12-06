import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random



def start_chrome0():
    user_agent = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69"
    ]
    UA = user_agent[random.randrange(0, len(user_agent), 1)]
    option0 = Options()                         
    # option.add_argument('--headless') 
    option0.add_argument('--user-data-dir=' + os.path.join(os.getcwd(),"profile0")) 
    option0.add_argument('--lang=ja-JP')
    option0.add_argument('--user-agent=' + UA)
    option0.add_argument('--ignore-certificate-errors')
    option0.add_argument('--ignore-ssl-errors')
    option0.add_argument("window-size=900,800")
    #ここで、バージョンなどのチェックをする
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option0) 

    return driver  

def start_chrome1():
    user_agent = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69"
    ]
    UA = user_agent[random.randrange(0, len(user_agent), 1)]
    option1 = Options()                         
    # option.add_argument('--headless') 
    option1.add_argument('--user-data-dir=' + os.path.join(os.getcwd(),"profile1")) 
    option1.add_argument('--lang=ja-JP')
    option1.add_argument('--user-agent=' + UA)
    option1.add_argument('--ignore-certificate-errors')
    option1.add_argument('--ignore-ssl-errors')
    option1.add_argument("window-size=900,800")
    #ここで、バージョンなどのチェックをする
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option1) 

    return driver  

def start_chrome2():
    user_agent = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69"
    ]
    UA = user_agent[random.randrange(0, len(user_agent), 1)]
    option2 = Options()                         
    # option.add_argument('--headless') 
    option2.add_argument('--user-data-dir=' + os.path.join(os.getcwd(),"profile2")) 
    option2.add_argument('--lang=ja-JP')
    option2.add_argument('--user-agent=' + UA)
    option2.add_argument('--ignore-certificate-errors')
    option2.add_argument('--ignore-ssl-errors')
    option2.add_argument("window-size=900,800")
    #ここで、バージョンなどのチェックをする
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option2) 

    return driver  