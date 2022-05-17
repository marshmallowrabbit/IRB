import pandas as pd
import numpy as np
from datetime import datetime
import time
import sys

ohlc = 'ETH-15m-end-2022-04-22.csv'
tf = 15 #in minutes
PO = 0.75 #percentage of optimisation 
sl = 2880 #total sample length in candles 

def Split(file_name, timeframe, pct_opt, sample_length):
    print('Splitting...')
    frame_lenth = len(1 for row in (open(file_name)))
    # timeframe
    # pct_opt
    # sample_length
    for i in range(1,frame_lenth,sample_length):
        frame = pd.read_csv(file_name, header=None,nrows=sample_length,skiprows=i)
        sample_csv_name = str(i) + 'file_name'
        df.to_csv(sample_csv_name,index=False,header=False,mode='a',chunksize=sample_length)

Split(ohlc,tf,PO,sl)
    
    

# #number_lines = sum(1 for row in (open(in_csv)))
# for i in range(1,number_lines,rowsize):
#     df = pd.read_csv(in_csv,
#           header=None,
#           nrows = rowsize,#number of rows to read at each loop
#           skiprows = i)#skip rows that have been read
#     out_csv = 'input' + str(i) + '.csv'
#     df.to_csv(out_csv,
#           index=False,
#           header=False,
#           mode='a',
#           chunksize=rowsize)
    
    