from bs4 import BeautifulSoup
from urllib.request import urlopen,Request;

fin_url='https://finviz.com/quote.ashx?t='
#https://finviz.com/quote.ashx?t=AAPL&p=d
tickers=['AMZN','FB','AAPl']

for ticker in tickers:
    url =fin_url+ticker
    req =Request(url=url,headers={'user-agaent':'Api'})
    response = urlopen(req)
    print(response)
    break