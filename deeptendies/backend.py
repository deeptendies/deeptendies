import sqlite3
import pandas as pd


class Database():
    def __init__(self, *args, **kwargs):
        try:
            self.conn = sqlite3.connect('sqlite.db')
        except Exception as e:
            print(e)
        print('sqlite.db connection established')

    def execute(self, query, *args, **kwargs):
        query_cursor = self.conn.cursor()
        query_cursor.execute(query, *args, **kwargs)
        return query_cursor.fetchall()

    def save(self, df, name):
        df.to_sql(name.lower(), self.conn, if_exists='replace')

    def read(self, name):
        return pd.read_sql(f'SELECT * FROM {name.lower()};', con=self.conn)

    def getall(self, tickers):
        union_block = """SELECT '{}' ticker, * FROM {}"""
        blocks = [union_block.format(x.lower(), x.lower()) for x in tickers]
        query = ' UNION ALL '.join(blocks)
        return pd.read_sql(query, con=self.conn)
