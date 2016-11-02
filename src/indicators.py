import pandas as pd


def simple_moving_average(series, window=14):
    return series.rolling(window).mean()


def exponential_moving_average(series, window=14):
    return series.ewm(span=window).mean()


def relative_strength_index(series, window=14, average_type="SMA"):
    delta = series.fillna(0).diff()[1:]
    ups = delta.copy()
    downs = delta.copy()
    ups[ups < 0] = 0
    downs[downs > 0] = 0

    if average_type == "EMA":
        rolling_ups = exponential_moving_average(ups, window)
        rolling_downs = exponential_moving_average(downs.abs(), window)
    else:
        rolling_ups = simple_moving_average(ups, window)
        rolling_downs = simple_moving_average(downs.abs(), window)

    rs = rolling_ups / rolling_downs
    rsi = 100.0 - (100.0 / (1.0 + rs))

    return rsi


def average_true_range(df, window=14):
    new_df = pd.DataFrame()
    new_df["atr1"] = (df["High"] - df["Low"]).abs()
    new_df["atr2"] = (df["High"] - df["Close"].shift()).abs()
    new_df["atr3"] = (df["Low"] - df["Close"].shift()).abs()
    return simple_moving_average(new_df[["atr1", "atr2", "atr3"]].max(axis=1), window)


def average_directional_index(df, window=14):
    up_move = df["High"].fillna(0).diff()
    down_move = df["Low"].fillna(0).diff()
    plus_dm = up_move.copy()
    minus_dm = down_move.copy()
    plus_dm[up_move < down_move] = 0
    plus_dm[up_move < 0] = 0

    minus_dm[down_move < up_move] = 0
    minus_dm[down_move < 0] = 0

    atr = average_true_range(df)

    plus_di = 100 * simple_moving_average(plus_dm, window).fillna(0) / atr
    minus_di = 100 * simple_moving_average(minus_dm, window).fillna(0) / atr

    return 100 * simple_moving_average((plus_di - minus_di).abs() / (plus_di + minus_di), window)
