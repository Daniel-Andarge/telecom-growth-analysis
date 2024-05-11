import psycopg2
import pandas as pd
import os
import sys


def sql_to_dataframe(conn, query):
    
    #Import data from a PostgreSQL database using a SELECT query
    cursor = conn.cursor()   
    try:
        cursor.execute(query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1
    # The execute returns a list of tuples:   
    tuples_list = cursor.fetchall()   
    
    # Transform the list into a pandas DataFrame:   
    df = pd.DataFrame(tuples_list, columns=[col[0] for col in cursor.description])
    cursor.close()   
    return df


def find_missing_values(df):
    missing_values = df.isnull().sum()
    print(missing_values)
    return missing_values
    


def handle_missing_values(df):
    numeric_columns = df.select_dtypes(include=['float64']).columns
    text_columns = df.select_dtypes(include=['object']).columns

    df_filled = df.copy()

    numeric_columns = numeric_columns.drop('MSISDN/Number')

    df_filled[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
    df_filled[text_columns] = df[text_columns].fillna('N/A')

    # Remove rows with empty 'MSISDN/Number'
    df_filled = df_filled.dropna(subset=['MSISDN/Number'])

    return df_filled



def handdle_outliers(df):



    return df_cleaned



def save_dataset(df, output_folder):

    # Create  output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    df_processed = handle_missing_values(df)

    # Save cleaned dataset
    output_path = os.path.join(output_folder, 'cleaned_dataset.csv')
    df_processed.to_csv(output_path, index=False)

    print(f"Cleaned dataset saved to {output_path}")
    return output_path


def load_dataset(path):
    try:
        # Get the path to the CSV file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, 'path')

        # Load the CSV file into a DataFrame
        df = pd.read_csv(csv_path)

        return df
    except FileNotFoundError as e:
        print(f"Error: {e}. The dataset file was not found.")
    except Exception as e:
        print(f"Error: {e}. An error occurred while loading the dataset.")

    return None

