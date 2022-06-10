def RandS(data_file_url,opt_ratio):
    data_list=[]
    # name=data_file[0:3]
    header = ['Timestamp', 'Open', 'High', 'Low', 'Close']
    # for file in os.listdir(data_file):
    #     if file.endswith('.csv'):
    #         data_list.append(file)
    # for file in data_list:
        # if str(number) in file:
        #     file_string = data_file+'/'+name+str(number)+'.csv'
    df = pd.read_csv(data_file_url)
    sample_length = len(df)
    in_sample_length = round(sample_length*opt_ratio)
    in_sample = pd.read_csv(data_file_url,nrows=in_sample_length)
    out_of_sample = pd.read_csv(data_file_url,names=header,skiprows=in_sample_length)
    return in_sample, out_of_sample
