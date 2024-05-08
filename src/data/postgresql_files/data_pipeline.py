import psycopg2
import pandas as pd

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
    
    # Now we need to transform the list into a pandas DataFrame:   
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

       # Replace missing values with the mean for numeric columns
    df_filled[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

     # Replace missing values with a placeholder for text columns
    df_filled[text_columns] = df[text_columns].fillna('N/A')

    return df_filled

