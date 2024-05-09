import pandas as pd


import pandas as pd

""" def aggregate_user_behavior(df):
    # Group the data by IMSI and aggregate the information
    df['Dur. (ms)'] = df['Dur. (ms)'].astype(float)
    grouped_data = df.groupby('IMSI').agg({'Dur. (ms)': 'count'})
    grouped_data.rename(columns={'Dur. (ms)': 'Number of xDR sessions'}, inplace=True)

    grouped_data['Session duration'] = df.groupby('IMSI')['Dur. (ms)'].sum()
    grouped_data['Total Download (DL) data'] = df.filter(like='DL').sum(axis=1)
    grouped_data['Total Upload (UL) data'] = df.filter(like='UL').sum(axis=1)
    grouped_data['Total Data Volume'] = df.filter(like='Bytes').sum(axis=1)

    return grouped_data """

def aggregate_user_behavior(df):
    # Group the data by IMSI and aggregate the information
    df['Dur. (ms)'] = df['Dur. (ms)'].astype(float)
    agg_functions = {
        'Dur. (ms)': 'count',
        'Session duration': 'sum',
        'Total Download (DL) data': 'sum',
        'Total Upload (UL) data': 'sum',
        'Total Data Volume': 'sum'
    }
    grouped_data = df.groupby('IMSI').agg(agg_functions)
    grouped_data.rename(columns={'Dur. (ms)': 'Number of xDR sessions'}, inplace=True)

    return grouped_data

