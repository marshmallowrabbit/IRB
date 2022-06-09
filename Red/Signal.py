def signals(df):
    Longs = []
    ExitLongs = []
    temp_long_stop = []
    temp_long_target = []
    # temp_long_stop = 0
    # temp_long_target = 0
    for i in range(len(df)):
        if 'y' in df['longOn'].iloc[i] and 'n' in df['longOn'].iloc[i-1]:
            if df['High'].iloc[i]>df['longlimit'].iloc[i]:
                Longs.append(df.iloc[i].name)
                # temp_long_stop = df.iloc[i].longstop.values
                # temp_long_target = df.iloc[i].longtarget.values
                temp_long_stop.append(df.iloc[i].longstop)
                temp_long_target.append(df.iloc[i].longtarget)
            # for j in range(len(df)-i):
            #     if df[''].iloc[i+j]<:
            #         ExitLongs.append(df.iloc[i+j].name)       
    return Longs,ExitLongs,temp_long_stop,temp_long_target

def signals(df):
    Longs = []
    ExitLongs = []
    temp_long_stop = 0
    temp_long_target = 0
    for i in range(len(df)):
        if 'y' in df['longOn'].iloc[i] and 'n' in df['longOn'].iloc[i-1] and df['High'].iloc[i]>df['longlimit'].iloc[i]:
            Longs.append(df.iloc[i].name)
            temp_long_stop = df.iloc[i].longstop
            temp_long_target = df.iloc[i].longtarget
        for j in range(len(df)-i):
            if df['Low'].iloc[i+j]<temp_long_stop or df['High'].iloc[i+j]>temp_long_target:
                ExitLongs.append(df.iloc[i+j].name)
            temp_long_stop = 0
            temp_long_target = 0
    return Longs,ExitLongs
l,el = signals(df)
