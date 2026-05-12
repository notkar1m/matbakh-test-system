import os
import psycopg2

def get_db_connection():
    # Vercel automatically provides POSTGRES_URL if using their storage
    conn = psycopg2.connect(os.environ.get('POSTGRES_URL'))
    return conn
