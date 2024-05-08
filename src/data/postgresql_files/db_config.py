import os
import sys
import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine

def load_env_variables():
    # Load env variables from .env file
    load_dotenv()

    # Access env variables
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    port = os.environ.get('PORT')
    database = os.environ.get('DATABASE')

    # Return db_config object
    db_config = {
        'user': user,
        'password': password,
        'host': host,
        'port': port,
        'database': database
    }
    return db_config



def db_connect(db_config):
    conn = None
    try:
        conn = psycopg2.connect(
              host=db_config['host'],
              database=db_config['database'],
              user=db_config['user'],
              password=db_config['password']
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        sys.exit(1)   
        
    print("All good, Connection successful!")
    return conn