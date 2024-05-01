# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:57:41 2024

@author: 112473
"""
import yfinance as yf
import pandas as pd

# 選擇的股票代碼列表
stocks = ['2330.TW', '2317.TW', '6505.TW', '2412.TW', '1301.TW', 
          '1303.TW', '1326.TW', '2882.TW', '2881.TW', '2002.TW']

# 設定起始和結束日期
start_date = '2020-01-01'
end_date = '2023-12-31'

# 創建一個空的DataFrame來儲存所有股票的資料
all_data = pd.DataFrame()

for stock in stocks:
    # 下載股票的日資料
    data = yf.download(stock, start=start_date, end=end_date)
    # 將股票代碼加入到DataFrame中
    data['Stock'] = stock
    # 將資料合併到all_data DataFrame中
    all_data = all_data.append(data)

# 重置索引
all_data.reset_index(inplace=True)

# 顯示資料
print(all_data.head())
all_data.to_csv("10stock.csv")
