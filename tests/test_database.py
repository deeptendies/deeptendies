#!/usr/bin/env python
"""Tests for `deeptendies` package."""
import pytest


def test_database():
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


def test_db_save():
    import deeptendies as dt
    db = dt.Database()
    # method 1
    df = dt.DataFrame.from_yf('SQQQ', db=db)
    print(db.read("SQQQ").head())

    # method 2
    df = dt.DataFrame.from_yf('GME')
    db.save(df, 'GME')
    print(db.read("GME").head())


def test_db_union():
    import deeptendies as dt
    db = dt.Database()
    # method 1
    dt.DataFrame.from_yf('GME', db=db)
    dt.DataFrame.from_yf('TSLA', db=db)
    dt.DataFrame.from_yf('TQQQ', db=db)
    df = db.getall(['GME', 'TSLA', 'TQQQ'])
    print(df.head())
    print(df.tail())


def test_backfill():
    import deeptendies as dt
    tickers = ['YINN', 'YANG', 'GME', 'TQQQ', 'SQQQ']
    db = dt.Database()
    dt.DataFrame.db_load(tickers, db=db)
    df = db.getall(tickers)
    print(df)
