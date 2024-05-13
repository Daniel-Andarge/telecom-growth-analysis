import psycopg2
import pandas as pd
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from scripts.shared.data_pipeline import (
    sql_to_dataframe,
    find_missing_values,
    handle_missing_values,
    handdle_outliers,
    save_dataset,
    load_dataset
)

class MockConnection:
    def cursor(self):
        return self

    def execute(self, query):
        pass

    def fetchall(self):
     
        return [(1, 'Daniel', 25), (2, 'Tekle', None), (3, 'BBB', 30)]

    def close(self):
        pass


class TestDataPipline(pd.DataFrame):

    def columns(self):
    
        return ['ID', 'Name', 'Age']

# Test sql_to_dataframe function
def test_sql_to_dataframe():
  
    conn = MockConnection()
    query = "SELECT * FROM users"

    df = sql_to_dataframe(conn, query)

    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == ['ID', 'Name', 'Age']
    assert df.values.tolist() == [[1, 'Daniel', 25], [2, 'Tekle', None], [3, 'BBB', 30]]


# Test find_missing_values function
def test_find_missing_values():

    df = TestDataPipline({'ID': [1, 2, 3], 'Name': ['Daniel', 'Tekle', 'BBB'], 'Age': [25, None, 30]})

    missing_values = find_missing_values(df)

    assert isinstance(missing_values, pd.Series)
    assert missing_values.tolist() == [0, 0, 1]


# Test handle_missing_values function
def test_handle_missing_values():
  
    df = TestDataPipline({'ID': [1, 2, 3], 'Name': ['Daniel', 'Tekle', None], 'Age': [25, None, 30]})

    df_filled = handle_missing_values(df)

    assert isinstance(df_filled, pd.DataFrame)
    assert df_filled.columns.tolist() == ['ID', 'Name', 'Age']
    assert df_filled.values.tolist() == [[1, 'Daniel', 25], [2, 'Tekle', 27.5], [3, 'N/A', 30]]


# Test save_dataset function
def test_save_dataset():

    df = TestDataPipline({'ID': [1, 2, 3], 'Name': ['Daniel', 'Tekle', 'BBB'], 'Age': [25, None, 30]})

    output_folder = 'output'
    filename = 'test_dataset.csv'

    output_path = save_dataset(df, output_folder, filename)
    assert os.path.exists(output_path)


# Test load_dataset function
def test_load_dataset():
    path = 'test_dataset.csv'
    df = load_dataset(path)

    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == ['ID', 'Name', 'Age']
    assert df.values.tolist() == [[1, 'Daniel', 25], [2, 'Tekle', None], [3, 'BBB', 30]]


