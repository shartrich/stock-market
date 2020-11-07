import datetime as dt
import pandas as pd
from utils.stocks import get_stock_single_date, get_f500_stocks
from utils.helpers.database import show_tables, show_databases, insert_df, do_query
from utils.configs.settings import DB_DATABASE, INPUT_PATH, OUTPUT_PATH


def test_single_stock():
    target_date = dt.datetime(2020, 10, 26)
    ticker = 'AAPL'    
    data = get_stock_single_date(ticker, target_date)
    print(data)


def new_db_table():
    f500_path = '{input_path}/f500.csv'.format(input_path=INPUT_PATH)
    df = pd.read_csv(f500_path)
    drop_query = 'DROP TABLE ;'.format(db=DB_DATABASE)
    query_res = do_query(drop_query, DB_DATABASE)
    print(query_res)
    insert_df(df, 'fortune_500', DB_DATABASE)


def test_f500_last_month():
    current_datetime = dt.datetime.utcnow()
    start_datetime = current_datetime - dt.timedelta(days=30)
    data = get_f500_stocks(start_datetime, current_datetime)
    df = pd.DataFrame(data, columns=data[0].keys())
    save_path = '{output_folder}/f500_test.csv'.format(output_folder=OUTPUT_PATH)
    df.to_csv(save_path, index=False)


if __name__ == '__main__':
    test_f500_last_month()
    

    

    