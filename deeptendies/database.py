import sqlite3

class Database():
    def __init__(self, *args, **kwargs):
        try:
            self.conn = sqlite3.connect('sqlite.db')
        except Exception as e:
            print(e)
        print("'/tmp/sqlite.db' connection established")
    def execute(self, query, *args, **kwargs):
        query_cursor = self.conn.cursor()
        query_cursor.execute(query, *args, **kwargs)
        return query_cursor.fetchall()
