def signals(df):
    Longs = []
    Shorts = []
    ExitLongs = []
    ExitShorts = []
    for i in range(len(df)):
        if 'y' in df['longOn'].iloc[i] and 'n' in df['longOn'].iloc[i-1] and inPosition == 0:
            if df['High'].iloc[i]>df['longlimit'].iloc[i]:
                Longs.append(df.iloc[i].name)
            for j in range range(len(df)-i):
                if 'y' in df['longOff'].iloc[i+j] and 'n' in df['longOff'].iloc[i+j-1]:
                    ExitLongs.append(df.iloc[i+j].name)       
    return Longs,ExitLongs
