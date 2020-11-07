import datetime as dt
import pandas as pd
import csv
import time as tm
from utils.yahoo_finance import export_stock_historical_data
from utils.configs.settings import INPUT_PATH


def file_format_datetime(datetime_value):
    return datetime_value.isoformat(timespec='seconds').replace(':','')


def get_stock_single_date(stock_ticker, target_datetime):
    """
    For a single stock get the metrics for a single day. Return key: value pairs as a dict
    """
    end_date = target_datetime + dt.timedelta(days=1)
    data = export_stock_historical_data(stock_ticker, target_datetime, end_date)
    # Zip the headers and the single data row into key: value dict
    return dict(zip(data[0], data[1]))



def get_f500_stocks(target_datetime, end_datetime):
    output = []
    f500_path = '{input_path}/f500.csv'.format(input_path=INPUT_PATH)
    with open(f500_path, "r", encoding='utf-8') as f500_file:
        reader = csv.reader(f500_file)
        for file_row in list(reader)[1:]:
            ticker = file_row[15]
            # ignore private companies
            if file_row[-1] != "Private":
                data = export_stock_historical_data(ticker, target_datetime, end_datetime)
                headers = ['Symbol'] + data[0]
                output.extend([dict(zip(headers, [ticker] + data_row)) for data_row in data[1:]])
    return output
