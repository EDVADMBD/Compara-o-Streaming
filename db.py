import sqlite3

def init_db():
    conn = sqlite3.connect("stream_prices.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            provider TEXT,
            plan TEXT,
            price REAL,
            currency TEXT,
            period TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_plans(plans):
    conn = sqlite3.connect("stream_prices.db")
    cur = conn.cursor()
    for p in plans:
        cur.execute('''
            INSERT INTO plans (provider, plan, price, currency, period)
            VALUES (?, ?, ?, ?, ?)
        ''', (p["provider"], p["plan"], p["price"], p["currency"], p["period"]))
    conn.commit()
    conn.close()
