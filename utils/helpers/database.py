from pymysql import connect, cursors
from sqlalchemy import create_engine
from utils.configs.settings import DB_USERNAME, DB_PASSWORD, DB_DATABASE, DB_HOST
from utils.helpers.ssh import create_tunnel


def create_connection(tunnel, database=DB_DATABASE):
    """connect to the DB with the user's credentials"""
    connection = connect(
        host=DB_HOST,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        db=database,
        port=tunnel.local_bind_port,
        cursorclass=cursors.DictCursor
    )
    return connection

def sql_engine(tunnel, database=DB_DATABASE):
    engine_string = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}".format(
            host=DB_HOST,
            user=DB_USERNAME,
            password=DB_PASSWORD,
            db=database,
            port=tunnel.local_bind_port,
        )
    return create_engine(
        engine_string,
        encoding='latin1', 
        # echo=True
        )


#show all of the tables in my database
def show_databases():
    with create_tunnel() as tunnel:
        conn = create_connection(tunnel)
        
        query = '''show databases;'''
        cursorObject = conn.cursor()
        cursorObject.execute(query)
        conn.close()
        return cursorObject.fetchall()

#show all of the tables in my database
def show_tables(database=DB_DATABASE):
    with create_tunnel() as tunnel:
        conn = create_connection(tunnel, database)
        
        query = '''show tables;'''
        cursorObject = conn.cursor()
        cursorObject.execute(query)
        conn.close()
        return cursorObject.fetchall()


def do_query(query, database):
    with create_tunnel() as tunnel:
        conn = create_connection(tunnel, database)
        cursorObject = conn.cursor()
        cursorObject.execute(query)
        conn.close()
        return cursorObject.fetchall()

def insert_df(df, table, database):
    with create_tunnel() as tunnel:
        # conn = create_connection(tunnel, database)
        conn = sql_engine(tunnel, database)
        df.to_sql(table, con=conn, if_exists="append", index=False)