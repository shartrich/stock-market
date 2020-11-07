import datetime as dt
import time as tm
import csv
import requests

YF_EXPORT_URL = 'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period_start}&period2={period_end}&interval=1d&events=history&includeAdjustedClose=true'


def get_csv_url(csv_url):
    """
    Take a csv url and return the data as a list of lists
    """
    with requests.Session() as s:
        download = s.get(csv_url)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        return list(cr)


def export_stock_historical_data(stock_ticker, start_datetime, end_datetime):
    """
    Take a stock ticker symbol, a datetime start, and a datetime end, 
    
    return yahoo finance daily data for time range as a list of lists
    """

    start_unix = int(tm.mktime(start_datetime.date().timetuple()))
    end_unix = int(tm.mktime(end_datetime.date().timetuple()))

    csv_url = YF_EXPORT_URL.format(
        ticker=stock_ticker,
        period_start=start_unix,
        period_end=end_unix
    )
    return get_csv_url(csv_url)
