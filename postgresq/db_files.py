import os
from dotenv import load_dotenv
import psycopg2
from sqlalchemy import create_engine

def load_db_config():
    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    user = os.environ['USER']
    password = os.environ['PASSWORD']
    host = os.environ['HOST']
    port = os.environ['PORT']
    database = os.environ['DATABASE']


""" # Usage
db_config = load_db_config()
print(db_config)
 """

def connect_to_db(db_config):
    conn = None
    try:
        conn = psycopg2.connect(
              host=db_config.host,
              database=db_config.database,
              user=db_config.user,
              password=db_config.password
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        sys.exit(1)   
        
    print("All good, Connection successful!")
    return conn