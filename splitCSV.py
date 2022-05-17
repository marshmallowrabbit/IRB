import pandas as pd
import numpy as np
from datetime import datetime
import time
import sys

ohlc = 'ETH-15m-end-2022-04-22.csv'
tf = 15 #timeframe in minutes
PO = 0.75 #percentage of optimisation 
sl = 2880*3 #total sample length in candles 
shift = 0.25 #percentage shift of sample_length

def Split(file_name, timeframe, pct_opt, sample_length, shift_by):
    print('Splitting...')
    frame_lenth = sum(1 for row in (open(file_name)))
    # timeframe
    # pct_opt
    # sample_length
    shift_candles = shift_by*sample_length
    n=0
    header = ['Timestamp', 'Open', 'High', 'Low', 'Close']
    for i in range(1,frame_lenth,shift_candles):
        n += 1
        frame = pd.read_csv(file_name,columns=header,nrows=sample_length,skiprows=i)
        sample_csv_name = str(n) + '.csv'
        frame.to_csv(sample_csv_name,index=False,mode='a',chunksize=sample_length)

Split(ohlc,tf,PO,sl,shift)
    
    
