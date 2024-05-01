# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:57:41 2024

@author: 112473
"""
import yfinance as yf

# 股票代號列表
stock_list = ['2330.TW', '2317.TW', '6505.TW', '2412.TW',
              '1301.TW', '1303.TW', '1326.TW', '2882.TW',
              '2881.TW', '2002.TW']

# 抓取每檔股票的日資料並輸出至CSV
for stock in stock_list:
    stock_code = stock.split('.')[0]  # 获取股票代码的数字部分
    data = yf.download(stock, start="2020-01-01", end="2023-12-31")
    data.to_csv(f"{stock_code}.csv")
