
import psycopg2
import os

#pyrefly: ignore[mising-import]
from dotenv import load_dotenv

#load en variables from .env file
load_dotenv()


def get_connection():

    try:

        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        return conn
    
    except Exception as e:
            
        print(f"Error connecting to database: {e}")
        
        return None