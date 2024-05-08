import os
from dotenv import load_dotenv

def load_db_config():
    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    user = os.environ['USER']
    password = os.environ['PASSWORD']
    host = os.environ['HOST']
    port = os.environ['PORT']
    database = os.environ['DATABASE']

    return {
        'user': user,
        'password': password,
        'host': host,
        'port': port,
        'database': database
    }

# Usage
db_config = load_db_config()
print(db_config)