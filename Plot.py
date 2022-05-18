import ccxt
import pandas as pd
import pandas_ta as ta
import numpy as np
from datetime import datetime
import time
import sys

def Plot(ohlc,Longs,Shorts,ExitLongs,ExitShorts):
    plt.figure(figsize=(12,5))
    plt.scatter(ohlc.loc[Longs].index, ohlc.loc[Longs]['Close'], marker='^')
    plt.plot(ohlc['Close'], alpha=0.7)