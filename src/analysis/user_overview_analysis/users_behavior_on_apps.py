import pandas as pd

# Sample xDR data
xdr_data = [
    {
        'IMSI': '123456789012345',
        'Session Duration': 3600,
        'Social Media DL (Bytes)': 100000,
        'Social Media UL (Bytes)': 50000,
        'YouTube DL (Bytes)': 200000,
        'YouTube UL (Bytes)': 100000,
        'Netflix DL (Bytes)': 150000,
        'Netflix UL (Bytes)': 75000,
        'Google DL (Bytes)': 300000,
        'Google UL (Bytes)': 150000,
        'Email DL (Bytes)': 80000,
        'Email UL (Bytes)': 40000,
        'Gaming DL (Bytes)': 500000,
        'Gaming UL (Bytes)': 250000,
        'Other DL (Bytes)': 400000,
        'Other UL (Bytes)': 200000,
        'Total DL (Bytes)': 1200000,
        'Total UL (Bytes)': 600000
    },
    # Add more xDR records here...
]

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