# =====================================================
# @date 2023.05.17
# @author yuteng
# @file main.py
# =====================================================

import requests
import pandas as pd
import csv


def run():
    # url = 'https://iftp.chinamoney.com.cn/r/cms/www/chinamoney/html/bond/bondInfoSearch.html?_pageNo=1&pageSize=15&=bondType=100001&couponType=&issueYear=2023'
    url = 'https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    # info_dict = {
    #     "issueYear": "2023",
    #     "bondType": "100001",  # "bondDisplayType": "Treasury Bond"}]
    # }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    data_text = response.text
    # print(response.text)
    # table_data = data_text[data_text.find('<tbody>'):data_text.find('/tbody')]
    # print(table_data)
    tables = pd.read_html(data_text)
    print(tables)


if __name__ == '__main__':
    run()
