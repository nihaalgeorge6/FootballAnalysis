def clean_players(df):
    players = []
    for i in range(1, df.shape[0]+1):
        players.append(df['Player'].str.split('\\')[i][0])

    df['Player'] = players
    return df

def clean_nation(df):
    nations = []
    for i in range(1, df.shape[0]+1):
        nations.append(df['Nation'].str.split(' ')[i][-1])

    df['Nation'] = nations
    return df

def clean_position(df):
    df['Pos'] = df['Pos'].str[0:2]
    return df

def change_headers(df):
    i = -1
    for x in df.columns.to_list():
        i+=1
        if ':' in x:
            next
        else:
            name =  df.iloc[0,i]
            df.iloc[0,i] = x.split('.')[0] + "_" +  name
        
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    return df

def format_data(df):
    df = change_headers(df)
    df = df.drop(columns=['Rk', 'Matches'])
    df = clean_players(df)
    df = clean_nation(df)
    df = clean_position(df)
    return df
