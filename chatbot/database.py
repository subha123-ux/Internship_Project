
import sqlite3

def init_db():
    conn = sqlite3.connect("chatlog.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_input TEXT,
                    bot_response TEXT
                )''')
    conn.commit()
    conn.close()

def log_interaction(user_input, bot_response):
    conn = sqlite3.connect("chatlog.db")
    c = conn.cursor()
    c.execute("INSERT INTO logs (user_input, bot_response) VALUES (?, ?)", (user_input, bot_response))
    conn.commit()
    conn.close()
