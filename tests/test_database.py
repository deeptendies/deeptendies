#!/usr/bin/env python
"""Tests for `deeptendies` package."""
import pytest
from unittest import TestCase

class DatabaseTestSuite(TestCase):
    def test_database(self):
        """
        test database module
        :return:
        """
        import deeptendies as dt
        db = dt.Database()
        result = db.execute("""CREATE TABLE test (
        test_id int,
        test_column_a varchar(50),
        test_column_b varchar(50));""")
        print(result)
        result = db.execute("""SELECT * FROM test;""")
        print(result)
        assert result is not None


    def test_db_save(self):
        import deeptendies as dt
        db = dt.Database()
        # method 1
        df = dt.DataFrame.from_yf('SQQQ', db=db)
        print(db.read("SQQQ").head())

        # method 2
        df = dt.DataFrame.from_yf('GME')
        db.save(df, 'GME')
        result = db.read("GME").head()
        print(result )
        assert result is not None


    def test_db_union(self):
        import deeptendies as dt
        db = dt.Database()
        # method 1
        dt.DataFrame.from_yf('GME', db=db)
        dt.DataFrame.from_yf('TSLA', db=db)
        dt.DataFrame.from_yf('TQQQ', db=db)
        df = db.getall(['GME', 'TSLA', 'TQQQ'])
        print(df.head())
        print(df.tail())
        assert df is not None


    def test_backfill(self):
        import deeptendies as dt
        tickers = ['YINN', 'YANG', 'GME', 'TQQQ', 'SQQQ']
        df = dt.DataFrame.db_load(tickers)
        print(df)
        assert df is not None
