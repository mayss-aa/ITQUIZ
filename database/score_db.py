import sqlite3
from datetime import datetime

def create_table():
    conn = sqlite3.connect("scores.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS scores (
        player TEXT,
        score INTEGER,
        level TEXT,
        date TEXT
    )""")
    conn.commit()
    conn.close()

def save_score(player, score, level):
    conn = sqlite3.connect("scores.db")
    c = conn.cursor()
    c.execute("INSERT INTO scores VALUES (?, ?, ?, ?)",
              (player, score, level, datetime.now().strftime("%Y-%m-%d %H:%M")))
    conn.commit()
    conn.close()

def get_top_scores():
    conn = sqlite3.connect("scores.db")
    c = conn.cursor()
    c.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 5")
    results = c.fetchall()
    conn.close()
    return results

def get_all_scores():
    conn = sqlite3.connect("scores.db")
    c = conn.cursor()
    c.execute("SELECT * FROM scores ORDER BY date DESC")
    results = c.fetchall()
    conn.close()
    return results