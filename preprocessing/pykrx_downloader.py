from pykrx import stock
import pandas as pd
import time
import os

width = 320
pd.set_option('display.width', width)

if not os.path.exists('./data/market_stock_list.csv'):
    print("stock list downloading..")
    stock_list_df = pd.DataFrame(columns=['시장', '티커', '종목이름'])
    stock_market = ['KOSPI', 'KOSDAQ', 'KONEX']

    for stock_market_element in stock_market:
        for ticker in stock.get_market_ticker_list(market=stock_market_element):
            종목이름 = stock.get_market_ticker_name(ticker)
            stock_list_df = stock_list_df.append(pd.Series([stock_market_element, ticker, 종목이름], index=stock_list_df.columns),
                                             ignore_index=True)
            print(stock_market_element, ticker, 종목이름)
            time.sleep(1)

    stock_list_df.to_csv('./data/market_stock_list.csv')

