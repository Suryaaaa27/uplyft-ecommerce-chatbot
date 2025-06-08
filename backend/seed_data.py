import csv
import sqlite3
import os

CSV_FILE_PATH = 'products.csv'
DB_PATH = os.path.join("instance", "chatbot.db")


def seed_database():
    if not os.path.exists(CSV_FILE_PATH):
        print(f"❌ CSV file '{CSV_FILE_PATH}' not found.")
        return

    if not os.path.exists(DB_PATH):
        print(f"❌ Database file '{DB_PATH}' not found. Run 'database.py' first.")
        return

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        with open(CSV_FILE_PATH, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            total_inserted = 0

            for row in reader:
                try:
                    cursor.execute('''
                        INSERT OR IGNORE INTO products (name, description, price, category, stock)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (
                        row['name'],
                        row['description'],
                        float(row['price']),
                        row['category'],
                        int(row['stock'])
                    ))
                    total_inserted += 1
                except Exception as e:
                    print(f"⚠️ Skipping row due to error: {e} | Row: {row}")

        conn.commit()
        print(f"✅ Successfully seeded {total_inserted} products into the database.")

    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    seed_database()