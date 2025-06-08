import sqlite3
import os

DB_PATH = os.path.join("instance", "chatbot.db")


def init_db():
    os.makedirs("instance", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            category TEXT NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("✅ Database schema initialized.")


if __name__ == "__main__":
    init_db()