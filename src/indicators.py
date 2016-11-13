import pandas as pd
import numpy as np


def simple_moving_average(series, window=14):
    return series.rolling(window).mean()


def exponential_moving_average(series, window=14):
    return series.ewm(span=window).mean()


def moving_average_convergence_divergence(series):
    ema_12 = exponential_moving_average(series, 12)
    ema_26 = exponential_moving_average(series, 26)
    macd_line = ema_12 - ema_26
    signal_line = exponential_moving_average(macd_line, 9)
    macd_histogram = macd_line - signal_line
    return macd_line, signal_line, macd_histogram


def accumulation_distribution_line(df):
    close = df["Close"]
    high = df["High"]
    low = df["Low"]
    series_1 = [(close-low) - (high-close)]
    series_2 = [high-low]
    new_df = pd.DataFrame()
    return series_1


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


<<<<<<< HEAD
=======
def aroon_indicator(df, window=14):
    period = 5

    high = df["High"]
    low = df["Low"]

    highestHigh = pd.rolling_max(high, period)
    lowestLow = pd.rolling_min(low, period)

    maxIndex = high.index[
        high.rolling(period).apply(np.argmax)[(period - 1):].astype(float) + np.arange(len(high) - (period - 1))]
    minIndex = low.index[
        low.rolling(period).apply(np.argmax)[(period - 1):].astype(float) + np.arange(len(low) - (period - 1))]

    timeDelta_max = ((highestHigh.dropna().index - maxIndex) / np.timedelta64(1, 'D')).astype(int)
    timeDelta_min = ((lowestLow.dropna().index - minIndex) / np.timedelta64(1, 'D')).astype(int)

    aroon_up = 100 * (period - timeDelta_max)/period
    aroon_down = 100 * (period - timeDelta_min)/period


    return aroon_up

def stochastic_oscillator(df, window=14):
    period = 14

    high = df["High"]
    low = df["Low"]

    highestHigh = pd.rolling_max(high, period)
    lowestLow = pd.rolling_min(low, period)

    k = (df["Close"] - lowestLow)/(highestHigh - lowestLow) * 100

    return pd.rolling_mean(k,3)
>>>>>>> origin/master
