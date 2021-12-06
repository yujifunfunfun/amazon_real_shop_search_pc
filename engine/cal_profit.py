import pandas as pd


def biccamera_yodobashi_cal_profit(biccamera_item_data,yodobashi_item_data,amazon_price_url_list):
    cols = ['ビックカメラ商品名','ビックカメラ価格','ビックカメラ利益','ビックカメラURL','ヨドバシ商品名','ヨドバシ価格','ヨドバシ利益','ヨドバシURL']
    profit_df = pd.DataFrame(index=[], columns=cols)
    for biccamera_item,yodobashi_item,amazon_price_url in zip(biccamera_item_data,yodobashi_item_data,amazon_price_url_list):
        biccamera_profit = int(amazon_price_url[0]) - int(biccamera_item[1])
        yodobashi_profit = int(amazon_price_url[0]) - int(yodobashi_item[1])

        record = pd.Series([biccamera_item[0],biccamera_item[1],biccamera_profit,biccamera_item[2],yodobashi_item[0],yodobashi_item[1],yodobashi_profit,yodobashi_item[2]], index=profit_df.columns)
        profit_df = profit_df.append(record, ignore_index=True)
    profit_df.to_csv("~/Desktop/biccamera_yodobashi_profit.csv",encoding="utf_8-sig",index=False)
        

def edion_nojima_ks_cal_profit(edion_item_data,nojima_item_data,ks_item_data,amazon_price_url_list):
    cols = ['エディオン商品名','エディオン価格','エディオン利益','エディオンURL','ノジマ商品名','ノジマ価格','ノジマ利益','ノジマURL','ケーズ商品名','ケーズ価格','ケーズ利益','ケーズURL']
    profit_df = pd.DataFrame(index=[], columns=cols)
    for edion_item,nojima_item,ks_item,amazon_price_url in zip(edion_item_data,nojima_item_data,ks_item_data,amazon_price_url_list):

        edion_profit = int(amazon_price_url[0]) - int(edion_item[1])
        nojima_profit = int(amazon_price_url[0]) - int(nojima_item[1])
        ks_profit = int(amazon_price_url[0]) - int(ks_item[1])

        record = pd.Series([edion_item[0],edion_item[1],edion_profit,edion_item[2],nojima_item[0],nojima_item[1],nojima_profit,nojima_item[2],ks_item[0],ks_item[1],ks_profit,ks_item[2]], index=profit_df.columns)
        profit_df = profit_df.append(record, ignore_index=True)
    profit_df.to_csv("~/Desktop/edion_nojima_ks_profit.csv",encoding="utf_8-sig",index=False)
       

def rakuten_yahoo_kakaku_kojima_cal_profit(rakuten_item_data,yahoo_item_data,kakaku_item_data,kojima_item_data,amazon_price_url_list):
    cols = ['amazon商品名','amazonカート価格-FBA','amazonURL','楽天商品名','楽天価格','楽天利益','楽天URL','Yahoo商品名','Yahoo価格','Yahoo利益','YahooURL','価格com商品名','価格com価格','価格com利益','価格comURL','コジマ商品名','コジマ価格','コジマ利益','コジマURL']
    profit_df = pd.DataFrame(index=[], columns=cols)
    for rakuten_item,yahoo_item,kakaku_item,kojima_item,amazon_price_url in zip(rakuten_item_data,yahoo_item_data,kakaku_item_data,kojima_item_data,amazon_price_url_list):

        rakuten_profit = int(amazon_price_url[0]) - int(rakuten_item[1])
        yahoo_profit = int(amazon_price_url[0]) - int(yahoo_item[1])
        kakaku_profit = int(amazon_price_url[0]) - int(kakaku_item[1])
        kojima_profit = int(amazon_price_url[0]) - int(kojima_item[1])
        
        record = pd.Series([amazon_price_url[2],amazon_price_url[0],amazon_price_url[1],rakuten_item[0],rakuten_item[1],rakuten_profit,rakuten_item[2],yahoo_item[0],yahoo_item[1],yahoo_profit,yahoo_item[2],kakaku_item[0],kakaku_item[1],kakaku_profit,kakaku_item[2],kojima_item[0],kojima_item[1],kojima_profit,kojima_item[2]], index=profit_df.columns)
        profit_df = profit_df.append(record, ignore_index=True)
    profit_df.to_csv("~/Desktop/rakuten_yahoo_kakaku_kojima_profit.csv",encoding="utf_8-sig",index=False)

def yamada_cal_profit(yamada_item_data,amazon_price_url_list):
    cols = ['ヤマダ商品名','ヤマダ価格','ヤマダ利益','ヤマダURL']
    profit_df = pd.DataFrame(index=[], columns=cols)
    for yamada_item,amazon_price_url in zip(yamada_item_data,amazon_price_url_list):
        yamada_profit = int(amazon_price_url[0]) - int(yamada_item[1])

        record = pd.Series([yamada_item[0],yamada_item[1],yamada_profit,yamada_item[2]], index=profit_df.columns)
        profit_df = profit_df.append(record, ignore_index=True)
    profit_df.to_csv("~/Desktop/yamada_profit.csv",encoding="utf_8-sig",index=False)
        

        
if __name__ == "__main__":
    yamada_cal_profit()