import pandas as pd
import os
import matplotlib.pyplot as plt

def recallNum(data_file,number):
    data_file_ent = []
    for file in os.listdir(data_file):
        if file.endswith('.csv'):
            data_file_ent.append(file)
    for file in data_file_ent:
        if str(number) in file:
            df = pd.read_csv(data_file+'/'+'BTC'+str(number)+'.csv')
    return df
  
def visualise(df):
    #create figure
    plt.figure()

    #define width of candlestick elements
    width = .4
    width2 = .05

    #define up and down prices
    up = df[df.Close>=df.Open]
    down = df[df.Close<df.Open]

    #define colors to use
    col1 = 'green'
    col2 = 'red'

    #plot up prices
    plt.bar(up.Index,up.Close-up.Open,width,bottom=up.Open,color=col1)
    plt.bar(up.Index,up.High-up.Close,width2,bottom=up.Close,color=col1)
    plt.bar(up.Index,up.Low-up.Open,width2,bottom=up.Open,color=col1)

    #plot down prices
    plt.bar(down.Index,down.Close-down.Open,width,bottom=down.Open,color=col2)
    plt.bar(down.Index,down.High-down.Open,width2,bottom=down.Open,color=col2)
    plt.bar(down.Index,down.Low-down.Close,width2,bottom=down.Close,color=col2)

    #rotate x-axis tick labels
    plt.xticks(rotation=45, ha='right')

    #display candlestick chart
    plt.show()
    
