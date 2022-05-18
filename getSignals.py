import ccxt
import pandas as pd
import pandas_ta as ta
import numpy as np
from datetime import datetime
import time
import sys
from Analysis import Analysis

def getSignals(df):
    print('Getting signals...')
    Longs = []
    Shorts = []
    ExitLongs = []
    ExitShorts = []
    maxLen = 50
    for i in range(len(df)):
        if 'y' in df['longOn'].iloc[i] and 'n' in df['longOn'].iloc[i-1]:
            if df['High'].iloc[i]>df['longlimit'].iloc[i]:
                Longs.append(df.iloc[i].name)
                for j in range(1,maxLen):
                    if (df['High'].iloc[i+j]>df['longtarget'].iloc[i+j]) or (df['Low'].iloc[i+j]<df['longstop'].iloc[i+j]):
                        ExitLongs.append(df.iloc[i+j].name)
                        break
    for i in range(len(df)):
        if 'y' in df['shortOn'].iloc[i] and 'n' in df['shortOn'].iloc[i-1]:
            if df['Low'].iloc[i]>df['shortlimit'].iloc[i]:
                Shorts.append(df.iloc[i].name)
                for j in range(1,maxLen):
                    if (df['High'].iloc[i+j]>df['shortstop'].iloc[i+j]) or (df['Low'].iloc[i+j]<df['shortlimit'].iloc[i+j]):
                        ExitShorts.append(df.iloc[i+j].name)
                        break
    return Longs,Shorts,ExitLongs,ExitShorts