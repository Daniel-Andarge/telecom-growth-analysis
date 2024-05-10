import pandas as pd

def aggregate_customer_data(df):
    # Aggregate the required information per customer
    aggregated_data = df.groupby('MSISDN/Number').agg({
        'TCP DL Retrans. Vol (Bytes)': lambda x: x.mean(),
        'Avg RTT DL (ms)': lambda x: x.mean(),
        'Handset Type': lambda x: x.mode().iloc[0],
        'Avg Bearer TP DL (kbps)': lambda x: x.mean()
    }).reset_index()

    # Rename the columns 
    aggregated_data.rename(columns={
        'TCP DL Retrans. Vol (Bytes)': 'Avg_TCP_Retrans.',
        'Avg RTT DL (ms)': 'Avg_RTT',
        'Handset Type': 'Handset',
        'Avg Bearer TP DL (kbps)': 'Avg_Throughput'
    }, inplace=True)

    return aggregated_data



def compute_top_bottom_frequent_values(data):
    # Compute the top, bottom, and most frequent values for TCP
    top_tcp_values = data['Avg_TCP_Retrans.'].nlargest(10)
    bottom_tcp_values = data['Avg_TCP_Retrans.'].nsmallest(10)
    most_frequent_tcp_values = data['Avg_TCP_Retrans.'].value_counts().head(10)

    # Compute the top, bottom, and most frequent values for RTT
    top_rtt_values = data['Avg_RTT'].nlargest(10)
    bottom_rtt_values = data['Avg_RTT'].nsmallest(10)
    most_frequent_rtt_values = data['Avg_RTT'].value_counts().head(10)

    # Compute the top, bottom, and most frequent values for Throughput
    top_throughput_values = data['Avg_Throughput'].nlargest(10)
    bottom_throughput_values = data['Avg_Throughput'].nsmallest(10)
    most_frequent_throughput_values = data['Avg_Throughput'].value_counts().head(10)

    # Return the computed values as dictionaries
    return {
        'Top TCP Values': top_tcp_values,
        'Bottom TCP Values': bottom_tcp_values,
        'Most Frequent TCP Values': most_frequent_tcp_values,
        'Top RTT Values': top_rtt_values,
        'Bottom RTT Values': bottom_rtt_values,
        'Most Frequent RTT Values': most_frequent_rtt_values,
        'Top Throughput Values': top_throughput_values,
        'Bottom Throughput Values': bottom_throughput_values,
        'Most Frequent Throughput Values': most_frequent_throughput_values
    }

