import sqlite3
from datetime import datetime
from config import DB_name

conn = sqlite3.connect(DB_name)
cursor = conn.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXSTS income (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               user_id INTEGER,
               amount REAL,
               comment TEXT,
               date TEXT
               )
""")
conn.commit()