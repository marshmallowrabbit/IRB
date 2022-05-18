import os
import pandas as pd

def recall(data_file):
    data_file_ent = []
    for file in os.listdir(data_file):
        if file.endswith('.csv'):
            data_file_ent.append(file)
    for file in data_file_ent:
        if str(1) in file:
            df = pd.read_csv(data_file+'/'+'BTC'+str(1)+'.csv')
    return df
