import os
from flask import Flask, render_template
from .db import get_db_connection

app = Flask(__name__, 
            template_folder='templates', 
            static_folder='static')

@app.route('/')
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    # Example: fetching data from your Postgres table
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('index.html', db_version=db_version)

# Required for Vercel to treat this as a serverless function
app.debug = True
