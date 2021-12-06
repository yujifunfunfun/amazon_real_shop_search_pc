import pandas as pd
import re
import math

def load_item_name():
    df = pd.read_csv('~/Desktop/amazon.csv',usecols=['Model'])
    df = df.fillna('None')
    df = df.values.tolist()
    item_name_list = []
    for item_name in df:
        item_name_list.append(item_name[0])
    return item_name_list

def load_jan():
    df = pd.read_csv('~/Desktop/amazon.csv',usecols=['Product Codes: EAN'],dtype={"Product Codes: EAN": str})
    df = df.fillna(0)
    df = df.values.tolist()
    jan_list = []
    for jan in df:
        jan = str(jan[0])
        if ',' in jan:
            p = r'(.*?),'  
            jan = re.search(p, jan).group(1)     
        jan_list.append(jan)
    return jan_list

def load_buybox_asin_name():
    df = pd.read_csv('~/Desktop/amazon.csv',usecols=['ASIN','新品: 現在価格','商品名'])
    df = df.fillna('None')
    df = df.values.tolist()
    buybox_asin_name_list = []
    for buybox_asin_name in df:
        buybox = buybox_asin_name[1]
        buybox = re.sub(r'\D', '', buybox) 
        buybox_asin_name_list.append([buybox,buybox_asin_name[2],buybox_asin_name[0]])
    return buybox_asin_name_list


def join_csv():
    rakuten_yahoo_kakaku_kojima_profit_df = pd.read_csv("~/Desktop/rakuten_yahoo_kakaku_kojima_profit.csv")
    biccamera_yodobashi_profit_df = pd.read_csv("~/Desktop/biccamera_yodobashi_profit.csv")
    yamada_profit_df = pd.read_csv("~/Desktop/yamada_profit.csv")
    edion_nojima_ks_profit_df = pd.read_csv("~/Desktop/edion_nojima_ks_profit.csv")
    data_list = []
    data_list.append(rakuten_yahoo_kakaku_kojima_profit_df)
    data_list.append(biccamera_yodobashi_profit_df)
    data_list.append(yamada_profit_df)
    data_list.append(edion_nojima_ks_profit_df)
    
    df = pd.concat(data_list, axis=1, sort=True)

    df.to_csv("~/Desktop/profit.csv",encoding="utf_8-sig",index=False)

if __name__ == "__main__":
    load_jan()



