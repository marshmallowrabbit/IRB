def signals(df):
    Longs = []
    ExitLongs = []
    Shorts = []
    ExitShorts = []
#     temps
    temp_longstop = 0
    temp_longtarget = 0
    temp_shortstop = 0
    temp_shorttarget = 0
#     nested for loop
    for i in range(len(df)):
        if 'y' in df['longOn'].iloc[i] and 'n' in df['longOn'].iloc[i-1] and df['High'].iloc[i]>df['longlimit'].iloc[i]:
            Longs.append(df.iloc[i].Timestamp)
            temp_longstop = df.iloc[i].longstop
            temp_longtarget = df.iloc[i].longtarget
            for j in range(len(df)-i):
                if df['Low'].iloc[i+j]<temp_longstop or df['High'].iloc[i+j]>temp_longtarget:
                    ExitLongs.append(df.iloc[i+j].Timestamp)
                    temp_longstop = 0
                    temp_longtarget = 0
                    break
    for i in range(len(df)):
        if 'y' in df['shortOn'].iloc[i] and 'n' in df['shortOn'].iloc[i-1] and df['Low'].iloc[i]<df['shortlimit'].iloc[i]:
            Shorts.append(df.iloc[i].Timestamp)
            temp_shortstop = df.iloc[i].longstop
            temp_shorttarget = df.iloc[i].longtarget
            for j in range(len(df)-i):
                if df['Low'].iloc[i+j]<temp_shorttarget or df['High'].iloc[i+j]>temp_shortstop:
                    ExitShorts.append(df.iloc[i+j].Timestamp)
                    temp_shortstop = 0
                    temp_shorttarget = 0
                    break
    
    return Longs,ExitLongs,Shorts,ExitShorts
l,el,s,es = signals(df)
