import os
import psycopg2
from dotenv import load_dotenv

# load the env
load_dotenv()

# connect to the database include try catch

try:
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),  
        database=os.getenv("DB_NAME"),      
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),  
    )
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record)
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:    
    # closing database connection.
    if conn:
        cursor.close()
        conn.close()    

