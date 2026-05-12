import os
import psycopg2
from flask import *

app = Flask(__name__)

def get_db_connection():
    # os.environ.get matches the Key you set in Vercel
    conn_string = os.environ.get('POSTGRES_URL')
    return psycopg2.connect(conn_string)

@app.route('/test-db')
def test_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT NOW();')
        time = cur.fetchone()
        cur.close()
        conn.close()
        return f"Connected! Database time is: {time}"
    except Exception as e:
        return f"Connection failed: {e}"
@app.route('/')
def index():
    return render_template("index.html")
