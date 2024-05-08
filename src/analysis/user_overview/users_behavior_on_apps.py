import pandas as pd


def aggregate_user_behavior(xdr_data):
    # Load the xDR session data into a pandas DataFrame
    df = pd.DataFrame(xdr_data)

    # Group the data by IMSI and aggregate the information
    grouped_data = df.groupby('IMSI')['Session Duration'].count().reset_index()
    grouped_data.rename(columns={'Session Duration': 'Number of xDR sessions'}, inplace=True)

    grouped_data['Session duration'] = df.groupby('IMSI')['Session Duration'].sum()
    grouped_data['Total Download (DL) data'] = df.filter(like='DL').sum(axis=1)
    grouped_data['Total Upload (UL) data'] = df.filter(like='UL').sum(axis=1)
    grouped_data['Total Data Volume'] = df.filter(like='Bytes').sum(axis=1)

    return grouped_data

# Aggregate user behavior
user_behavior = aggregate_user_behavior(xdr_data)

# Print the aggregated information
print(user_behavior)