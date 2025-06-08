import sqlite3
import os

# Define the path to your SQLite database
DB_PATH = os.path.join("instance", "chatbot.db")

def get_distinct_categories():
    """
    Fetches all distinct categories from the 'products' table.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Execute the SQL query to get distinct categories
        cursor.execute("SELECT DISTINCT category FROM products")
        results = cursor.fetchall()

        # Extract categories from the result set
        categories = [row[0] for row in results]

        # Print or return the categories
        print("Distinct categories in the database:")
        for category in categories:
            print(category)

        return categories

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    get_distinct_categories()