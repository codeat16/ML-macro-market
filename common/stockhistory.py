import time
import datetime
import urllib.request
import re
import pandas as pd

YAHOO_DATA_DIR = '../data/yahoo_data/'

def Get_Yahoo_CSV(symbol='^GSPC', start = '2000-01-01', end = '2001-12-31'):
    ''' symbol: str of stock symbol
        start: start date in 1999-01-05 format
        end: end date in 2000-05-25 format
    '''
    df = pd.read_csv( YAHOO_DATA_DIR + symbol + '.csv',
        #dtype={'Close': float, 'Adj Close': float},
        parse_dates = ['Date'] ) # parse_dates = True does not work

    df = df[(df['Date'] >= start) & (df['Date'] <= end)]

    #set index useless, why?
    df2 = df.set_index('Date')
    return df2


def Get_Yahoo(symbol='YHOO', start = '2000-01-01', end = '2001-12-31'):
    ''' symbol: str of stock symbol
        start: start date in 1999-01-05 format
        end: end date in 2000-05-25 format
    '''
    date_start = datetime.datetime.strptime(start, "%Y-%m-%d").date()
    date_end = datetime.datetime.strptime(end, "%Y-%m-%d").date()
    tstamp_start = str(int(time.mktime(date_start.timetuple())))
    tstamp_end = str(int(time.mktime(date_end.timetuple())))

    request_url = r"https://finance.yahoo.com/quote/{0}/history?period1={1}&period2={2}&interval=1d&filter=history&frequency=1d".format(symbol, tstamp_start, tstamp_end)

    f = urllib.request.urlopen(request_url)
    response_str = f.read().decode('utf-8')
    re_result = re.search(r'"crumb":"(\w+)"', response_str)
    crumb = re_result.group(1)

    request_url_csv = r"https://query1.finance.yahoo.com/v7/finance/download/{0}?period1={1}&period2={2}&interval=1d&events=history&crumb={3}".format(symbol, tstamp_start, tstamp_end, crumb)
