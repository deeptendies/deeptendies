#!/usr/bin/env python

"""Tests for `deeptendies` package."""
import pytest


@pytest.fixture
def from_yf_info():
    """
    pytest fixture to get yahoo finance info
    :return:
    """
    from deeptendies.data import DataFrame
    dt = DataFrame()
    print(type(dt.from_yf_info('TQQQ')))
    print(dt.from_yf_info('TQQQ'))


@pytest.fixture
def from_yf():
    """
    pytest fixture to get dataframe from yahoo finance
    :return:
    """
    import deeptendies as dt
    return dt.DataFrame.from_yf('TQQQ')


def test_pipeline(from_yf):
    """
    test pipeline class, as well as a few feature engineering operators. then assert the dataframe's column with
    the expected values.
    :return:
    """
    import deeptendies as dt
    pipeline = dt.Pipeline(
        [
            dt.Feature.get_x_high,
            dt.Feature.get_x_low,
            dt.Feature.get_x_ma,
            dt.Feature.get_diff
        ]
    )
    df = pipeline.run(df=from_yf, x=50)
    df = pipeline.run(df=df, x=100)
    df = pipeline.run(df=df, x=200)
    df = pipeline.run(df=df, x=50, interval='week')
    df = pipeline.run(df=df, x=100, interval='week')
    df = pipeline.run(df=df, x=200, interval='week')
    print(df.head())
    print(df.columns)
    expected = ['high', 'low', 'open', 'close', 'volume', 'adj_close', '50_day_high',
                '50_day_low', '50_day_ma', 'high_diff', 'low_diff', 'close_diff',
                'volume_diff', '100_day_high', '100_day_low', '100_day_ma',
                '200_day_high', '200_day_low', '200_day_ma', '50_week_high',
                '50_week_low', '50_week_ma', '100_week_high', '100_week_low',
                '100_week_ma', '200_week_high', '200_week_low', '200_week_ma']
    assert all([a == b for a, b in zip(df.columns, expected)])  # https://codefrom.page.link/RtQw
