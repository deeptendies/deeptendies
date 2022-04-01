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
