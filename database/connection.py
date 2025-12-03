import os   # Import var
from dotenv import load_dotenv  # Import connection var
import psycopg  # Connection Database

load_dotenv()   # Start var

# Local var
user = os.getenv('db_user') 
pwd = os.getenv('db_pass')

connect = psycopg.connect(
    f'postgresql://{user}:{pwd}@localhost/library'
)

# Testing connection
cursor = connect.cursor()