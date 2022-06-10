def signals(df):
    Longs = []
    Long_wins = []
    Long_losses = []
    Shorts = []
    Short_wins = []
    Short_losses = []
#     temps
    temp_longstop = 0
    temp_longtarget = 0
    temp_shortstop = 0
    temp_shorttarget = 0
#     nested for loop
    for i in range(len(df)):
        if 'y' in df['longOn'].iloc[i] and 'n' in df['longOn'].iloc[i-1] and df['High'].iloc[i]>df['longlimit'].iloc[i]:
            Longs.append(df.iloc[i].name)
            temp_longstop = df.iloc[i].longstop
            temp_longtarget = df.iloc[i].longtarget
            for j in range(len(df)-i):
                if df['Low'].iloc[i+j]<temp_longstop:
                    Long_losses.append(df.iloc[i+j].name)
                    break
                elif df['High'].iloc[i+j]>temp_longtarget:
                    Long_wins.append(df.iloc[i+j].name)
                    break
    for i in range(len(df)):
        if 'y' in df['shortOn'].iloc[i] and 'n' in df['shortOn'].iloc[i-1] and df['Low'].iloc[i]<df['shortlimit'].iloc[i]:
            Shorts.append(df.iloc[i].name)
            temp_shortstop = df.iloc[i].longstop
            temp_shorttarget = df.iloc[i].longtarget
            for j in range(len(df)-i):
                if df['Low'].iloc[i+j]<temp_shorttarget:
                    Short_wins.append(df.iloc[i+j].name)
                    break
                elif df['High'].iloc[i+j]>temp_shortstop:
                    Short_losses.append(df.iloc[i+j].name)
                    break
    
    return Longs,Long_wins,Long_losses,Shorts,Short_wins,Short_losses
ls,lws,lls,ss,sws,sls = signals(df)
