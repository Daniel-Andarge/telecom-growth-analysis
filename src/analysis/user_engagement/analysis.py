import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def aggregate_engagement_metrics(df):
    # aggrregate engagement metrics per customer MSISDN/Number
    aggregated_data = df.groupby('MSISDN/Number').agg({
        'Dur. (ms)': 'sum',
        'Bearer Id': 'count',
        'Total UL (Bytes)': 'sum',
        'Total DL (Bytes)': 'sum'
    }).reset_index()

    column_mapping = {
        'Bearer Id': 'Bearer_Id',
        'Dur. (ms)': 'Duration',
        'Total DL (Bytes)': 'Total_DL',
        'Total UL (Bytes)': 'Total_UL'
    }

    aggregated_data.rename(columns=column_mapping, inplace=True)
    return aggregated_data



def get_top_ten_customers(aggregated_data):
        
    aggregated_data['Rank_Duration'] = aggregated_data['Duration'].rank(ascending=False)
    aggregated_data['Rank_Sessions'] = aggregated_data['Bearer_Id'].rank(ascending=False)
    aggregated_data['Rank_Traffic'] = (aggregated_data['Total_UL'] + aggregated_data['Total_DL']).rank(ascending=False)
    
    top_10_duration = aggregated_data.nlargest(10, 'Rank_Duration')
    top_10_sessions = aggregated_data.nlargest(10, 'Rank_Sessions')
    top_10_traffic = aggregated_data.nlargest(10, 'Rank_Traffic')
    
    top_10_duration_list = top_10_duration['MSISDN/Number'].tolist()
    top_10_sessions_list = top_10_sessions['MSISDN/Number'].tolist()
    top_10_traffic_list = top_10_traffic['MSISDN/Number'].tolist()
    
    return {
        'Top 10 Duration': top_10_duration_list,
        'Top 10 Sessions': top_10_sessions_list,
        'Top 10 Traffic': top_10_traffic_list
    }



def engagement_classification(aggregated_data)
    engagement_metrics = ['Duration', 'Bearer_Id', 'Total_UL', 'Total_DL']

    # Normalize the engagement metrics using StandardScaler
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(aggregated_data[engagement_metrics])

   
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(normalized_data)

    cluster_labels = kmeans.labels_
    aggregated_data['Cluster'] = cluster_labels

    return aggregated_data



def compute_cluster_metrics(classified_data, Metric):
    # Group the data by the cluster labels
    grouped_data = classified_data.groupby('Cluster')

    cluster_metrics = []

    # Compute the metrics for each cluster
    for cluster_label, group in grouped_data:
        metrics = {
            'Cluster': cluster_label,
            'Minimum': group[Metric].min(),
            'Maximum': group[Metric].max(),
            'Average': group[Metric].mean(),
            'Total': group[Metric].sum()
        }
        cluster_metrics.append(metrics)

    return pd.DataFrame(cluster_metrics)




def get_top_10_engaged_users(original_data, aggregated_data):
    # Merge aggregated_data with the original data
    merged_data = pd.merge(original_data, aggregated_data, on='MSISDN/Number')

    # Derive the top 10 most engaged users per application
    top_10_engaged_users = merged_data.groupby('Bearer Id').apply(lambda x: x.nlargest(10, 'Avg Bearer TP DL (kbps)')).reset_index(drop=True)

    return top_10_engaged_users



def visualize_top_three_apps(top_10_users):

  # Calculate the count of each application
    application_counts = top_10_users['Bearer Id'].value_counts().head(3)

   # Create a bar chart
    plt.bar(application_counts.index, application_counts.values)

   # Set the chart title and axis labels
    plt.title('Top 3 Most Used Applications')
    plt.xlabel('Application')
    plt.ylabel('Usage Count')

    plt.show()

