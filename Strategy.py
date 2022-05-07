import ccxt
import pandas as pd
import pandas_ta as ta
import numpy as np
from datetime import datetime
import time
import sys



ohlc = 'TEST.csv' #filename

def Analysis(file_name):
    c = 45/100
    riskratio = 1.5
    print('Analyzing...')
    df = pd.read_csv(file_name)
    df['a'] = abs(df.apply(lambda row: row.High - row.Low, axis=1))
    df['b'] = abs(df.apply(lambda row: row.Close - row.Open, axis=1))
    df['ca'] = df.apply(lambda row: row.a * c, axis=1)
    df['rv'] = np.where(df['b'].values < df['ca'].values,1,0)
    df['x'] = df.apply(lambda row: row.Low + row.ca, axis=1)
    df['y'] = df.apply(lambda row: row.High - row.ca, axis=1)
    df['sl'] = np.where((df['High'].values>df['y'].values) & (df['Close'].values<df['y'].values) & (df['Open'].values<df['y'].values),1,0)
    df['ss'] = np.where((df['Low'].values<df['x'].values) & (df['Close'].values>df['x'].values) & (df['Open'].values>df['x'].values),1,0)
    df['hc'] = df.High - df.Low
    df['hcs'] = abs(df.High-df.Close.shift(1))
    df['lcs'] = abs(df.Low-df.Close.shift(1))
    df['rt'] = df[['hc','hcs','lcs']].max(axis=1)
    df['slow'] = ta.sma(df['Close'],5)
    df['fast'] = ta.ema(df['Close'],18)
    df['trend 1'] = ta.sma(df['Close'],50)
    df['trend 2'] = ta.sma(df['Close'],89)
    df['trend 3'] = ta.ema(df['Close'],144)
    df['mid'] = ta.ema(df['Close'],35)
    df['low'] = ta.ema(df['Close'],35) + 0.5*(ta.rma(df['rt'],35))
    df['longOn'] = np.where((df.slow.values>df.fast.values)&(df['trend 1'].values<df.fast.values)&(df['trend 2'].values<df.fast.values)&(df['trend 3'].values<df.fast.values)&(df['mid'].values<df.fast.values)&(df['low'].values<df.fast.values),1,0)
    df['shortOn'] = np.where((df.slow.values<df.fast.values)&(df['trend 1'].values>df.fast.values)&(df['trend 2'].values>df.fast.values)&(df['trend 3'].values>df.fast.values)&(df['mid'].values>df.fast.values)&(df['low'].values>df.fast.values),1,0)
    return df

print(Analysis(ohlc))

