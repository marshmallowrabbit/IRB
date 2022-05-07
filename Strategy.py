import ccxt
import pandas as pd
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
    print(df)
    df['a'] = abs(df.apply(lambda row: row.High - row.Low, axis=1))
    df['b'] = abs(df.apply(lambda row: row.Close - row.Open, axis=1))
    df['ca'] = df.apply(lambda row: row.a * c, axis = 1)
    df['rv'] = np.where(df['b'].values < df['ca'].values,1,0)
    df['x'] = df.apply(lambda row: row.Low + row.ca, axis = 1)
    df['y'] = df.apply(lambda row: row.High - row.ca, axis = 1)
    df['sl'] = np.where((df['High'].values>df['y'].values) & (df['Close'].values<df['y'].values) & (df['Open'].values<df['y'].values),1,0)
    df['ss'] = np.where((df['Low'].values<df['x'].values) & (df['Close'].values>df['x'].values) & (df['Open'].values>df['x'].values),1,0)
    print(help(ta.sma(df.Close)))
    df['slow'] = df.ta.sma(close=df['Close'].values,length=5)
    # df['fast'] = df.ta.ema(df['Close'].values,18)
    # df['trend 1'] = df.sma(df['Close'].values,50)
    # df['trend 2'] = df.sma(df['Close'].values,89)
    # df['trend 3'] = df.ema(df['Close'].values,144)
    # df['mid'] = df.ema(df['Close'].values,35)
    # df['low'] = df.ema(df['Close'].values,35)# + 0.5*(df.ta.rma)

    return df

print(Analysis(ohlc))

