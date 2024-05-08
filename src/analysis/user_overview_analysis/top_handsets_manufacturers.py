

import pandas as pd
from collections import Counter


def get_top_handsets(xdr_df):
    
    # Group by Handset Manufacturer and Handset Type and count 
    handset_counts = xdr_df.groupby(['Handset Manufacturer', 'Handset Type']).size().reset_index(name='Count')

    # Sort the counts in descending order
    sorted_handsets = handset_counts.sort_values(by='Count', ascending=False)

    # Top 10 handsets
    top_10_handsets = sorted_handsets.head(10)

    # Return a list
    return top_10_handsets[['Handset Manufacturer', 'Handset Type']].values.tolist()




def get_top_handset_manufacturers(xdr_data, top_n=3):
    # Load the xDR session data into a pandas DataFrame
    df = pd.DataFrame(xdr_data)

    # Group the data by Handset Manufacturer and count the occurrences
    manufacturer_counts = df['Handset Manufacturer'].value_counts().reset_index()

    # Rename the columns
    manufacturer_counts.columns = ['Handset Manufacturer', 'Count']

    # Sort the counts in descending order
    sorted_manufacturers = manufacturer_counts.sort_values(by='Count', ascending=False)

    # Get the top n handset manufacturers
    top_manufacturers = sorted_manufacturers.head(top_n)

    # Return the top handset manufacturers as a list
    return top_manufacturers['Handset Manufacturer'].tolist()



def identify_top_handsets(top_manufacturers, xdr_data):
    # Load the xDR session data into a pandas DataFrame
    df = pd.DataFrame(xdr_data)

    # Create a dictionary to store the top handsets per manufacturer
    top_handsets_per_manufacturer = {}

    # Iterate over the top manufacturers
    for manufacturer in top_manufacturers:
        # Filter the data for the current manufacturer
        manufacturer_data = df[df['Handset Manufacturer'] == manufacturer]

        # Get the top 5 handsets for the current manufacturer
        handset_counts = Counter(manufacturer_data['Handset Type'])
        top_handsets = handset_counts.most_common(5)
        top_handsets_per_manufacturer[manufacturer] = [handset for handset, _ in top_handsets]

    return top_handsets_per_manufacturer


# Example usage
xdr_data = [
    {'Bearer ID': '123456', 'Dur. (ms)': 5000, 'Start': '2022-01-01 10:00:00', 'Handset Manufacturer': 'Apple', 'Handset Type': 'iPhone 12'},
    {'Bearer ID': '789012', 'Dur. (ms)': 6000, 'Start': '2022-01-01 11:00:00', 'Handset Manufacturer': 'Samsung', 'Handset Type': 'Galaxy S20'},
    {'Bearer ID': '345678', 'Dur. (ms)': 7000, 'Start': '2022-01-01 12:00:00', 'Handset Manufacturer': 'Apple', 'Handset Type': 'iPhone 11'},
    {'Bearer ID': '901234', 'Dur. (ms)': 8000, 'Start': '2022-01-01 13:00:00', 'Handset Manufacturer': 'Huawei', 'Handset Type': 'P30'},
    {'Bearer ID': '567890', 'Dur. (ms)': 9000, 'Start': '2022-01-01 14:00:00', 'Handset Manufacturer': 'Samsung', 'Handset Type': 'Galaxy S21'},
    {'Bearer ID': '234567', 'Dur. (ms)': 10000, 'Start': '2022-01-01 15:00:00', 'Handset Manufacturer': 'Apple', 'Handset Type': 'iPhone 12 Pro'},
]

# Get the top handset manufacturers
top_manufacturers = get_top_handset_manufacturers(xdr_data, top_n=3)

# Identify the top 5 handsets per top 3 handset manufacturers
top_handsets_per_manufacturer = identify_top_handsets(top_manufacturers, xdr_data)

# Print the top 5 handsets per top 3 handset manufacturers
for manufacturer, handsets in top_handsets_per_manufacturer.items():
    print(f"\nTop 5 Handsets for {manufacturer}:")
    for handset in handsets:
        print(handset)