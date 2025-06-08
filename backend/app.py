from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import sqlite3
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Define paths
DB_PATH = os.path.join("instance", "chatbot.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    return conn, cursor

@app.route('/')
def home():
    """
    Serve the chatbot UI (index.html)
    """
    return send_from_directory(directory='static', path='index.html')

@app.route('/api/products', methods=['GET'])
def search_products():
    query = request.args.get('q', '').strip().lower()
    category = request.args.get('category', None)

    if not query and not category:
        return jsonify({"error": "Either 'q' or 'category' must be provided."}), 400

    try:
        conn, cursor = get_db_connection()

        sql_query = "SELECT * FROM products WHERE 1=1"
        params = []

        if query:
            sql_query += " AND name LIKE ?"
            params.append(f"%{query}%")

        if category:
            sql_query += " AND LOWER(category) = ?"
            params.append(category.lower())

        cursor.execute(sql_query, params)
        results = cursor.fetchall()

        products = [
            {
                "id": r[0],
                "name": r[1],
                "description": r[2],
                "price": r[3],
                "category": r[4],
                "stock": r[5]
            }
            for r in results
        ]

        conn.close()
        return jsonify(products)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)