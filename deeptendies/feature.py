class Feature:
    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def get_x_low(df, x=52, interval='day', **kwargs):
        if interval == 'week':
            x_inter = x * 7
        elif interval == 'day':
            x_inter = x
        df[f'{x}_{interval}_low'] = df['low'].rolling(window=x_inter, min_periods=x_inter).min()
        return df

    @staticmethod
    def get_x_high(df, x=52, interval='day', **kwargs):
        if interval == 'week':
            x_inter = x * 7
        elif interval == 'day':
            x_inter = x
        df[f'{x}_{interval}_high'] = df['high'].rolling(window=x_inter, min_periods=x_inter).max()
        return df

    @staticmethod
    def get_x_ma(df, x=50, interval='day', **kwargs):
        if interval == 'week':
            x_inter = x * 7
        elif interval == 'day':
            x_inter = x
        df[f'{x}_{interval}_ma'] = df['close'].rolling(window=x_inter, min_periods=x_inter).mean()
        return df

    @staticmethod
    def get_diff(df, cols=['high', 'low', 'close', 'volume'], **kwargs):
        for col in cols:
            df[f'{col}_diff'] = df[col].diff()
        return df
