import matplotlib.pyplot as plt
import pandas as pd
import requests
import json

plt.style.use('ggplot')


def graph_data(stock):
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=10y/json'
    res=requests.get(stock_price_url).text[30:-1].replace('\n','')
    j=json.loads(res)
    df=pd.DataFrame(j['series'])
    df['Date']=pd.to_datetime(df['Date'],format='%Y%m%d')
    plt.plot_date(df['Date'].tolist(), df['close'].tolist(),'-', label='价格')
    plt.xlabel('日期')
    plt.ylabel('价格')
    plt.title('股票价格走势')
    plt.legend()
    plt.show()

graph_data('TSLA')