
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def aggregate_user_behavio(df):
    aggregated_data = df.groupby('MSISDN/Number').agg({
        'Bearer Id': 'count',
        'Dur. (ms)': 'mean',  
        'Total DL (Bytes)': 'mean',  
        'Total UL (Bytes)': 'mean',  
        'Social Media DL (Bytes)': 'mean',  
        'Social Media UL (Bytes)': 'mean', 
        'Google DL (Bytes)': 'mean',  
        'Google UL (Bytes)': 'mean',  
        'Email DL (Bytes)': 'mean',  
        'Email UL (Bytes)': 'mean',  
        'Youtube DL (Bytes)': 'mean',  
        'Youtube UL (Bytes)': 'mean', 
        'Netflix DL (Bytes)': 'mean', 
        'Netflix UL (Bytes)': 'mean', 
        'Gaming DL (Bytes)': 'mean',  
        'Gaming UL (Bytes)': 'mean',  
        'Other DL (Bytes)': 'mean', 
        'Other UL (Bytes)': 'mean'  
    }).reset_index()

    column_mapping = {
        'Bearer Id': 'Bearer_Id',
        'Dur. (ms)': 'Duration',
        'Total DL (Bytes)': 'Total_DL',
        'Total UL (Bytes)': 'Total_UL',
        'Social Media DL (Bytes)': 'SM_DL',
        'Social Media UL (Bytes)': 'SM_UL',
        'Google DL (Bytes)': 'Google_DL',
        'Google UL (Bytes)': 'Google_UL',
        'Email DL (Bytes)': 'Email_DL',
        'Email UL (Bytes)': 'Email_UL',
        'Youtube DL (Bytes)': 'YouTube_DL',
        'Youtube UL (Bytes)': 'YouTube_UL',
        'Netflix DL (Bytes)': 'Netflix_DL',
        'Netflix UL (Bytes)': 'Netflix_UL',
        'Gaming DL (Bytes)': 'Gaming_DL',
        'Gaming UL (Bytes)': 'Gaming_UL',
        'Other DL (Bytes)': 'Other_DL',
        'Other UL (Bytes)': 'Other_UL'
    }

    aggregated_data.rename(columns=column_mapping, inplace=True)

    return aggregated_data



def analyze_basic_metrics(df):

    metrics = df.drop("MSISDN/Number", axis=1).describe()

    return metrics





def perform_bivariate_analysis(df):
    # Select the columns for analysis
    # Exclude MSISDN/Number and Bearer_Id columns
    applications = df.columns[6:-2]  
    total_data = df['Total_DL'] + df['Total_UL']

    # Calculate the correlation coefficient for each application
    correlations = {}
    for app in applications:
        correlation = df[app].corr(total_data)
        correlations[app] = correlation

    # Sort the correlations in descending order
    sorted_correlations = sorted(correlations.items(), key=lambda x: abs(x[1]), reverse=True)

 
    for app, correlation in sorted_correlations:
        print(f"Correlation between {app} and Total DL+UL data: {correlation}")





def calculate_total_data_per_decile(user_data):
    # Calculate the total duration for all sessions for each user
    user_duration = user_data.groupby('MSISDN/Number')['Duration'].sum().reset_index()

    # Determine the decile thresholds for the total duration
    decile_thresholds = user_duration['Duration'].quantile([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]).tolist()

    user_duration['Decile_Class'] = pd.qcut(user_duration['Duration'], q=10, labels=False)

    top_five_deciles = user_duration[user_duration['Decile_Class'] >= 5]

    # Calculate the total data (DL+UL) per decile class
    decile_data = top_five_deciles.merge(user_data, on='MSISDN/Number')
    total_data_per_decile = decile_data.groupby('Decile_Class')[['Total_DL', 'Total_UL']].sum().reset_index()

    return total_data_per_decile


def perform_correlation_analysis(dataframe):
    # Create a subset of the dataset containing the relevant columns
    data_subset = dataframe[['SM_DL', 'SM_UL', 'Google_DL', 'Google_UL', 'Email_DL', 'Email_UL', 'YouTube_DL', 'YouTube_UL', 'Netflix_DL', 'Netflix_UL', 'Gaming_DL', 'Gaming_UL', 'Other_DL', 'Other_UL']]

    # Compute the correlation matrix
    correlation_matrix = data_subset.corr()

    return correlation_matrix