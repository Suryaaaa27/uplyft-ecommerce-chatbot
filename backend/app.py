from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import csv
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

def load_products():
    """
    Load products from products.csv into memory.
    """
    products = []
    try:
        with open('products.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                product = {
                    "id": int(row["id"]),
                    "name": row["name"].strip().lower(),
                    "description": row["description"].strip().lower(),
                    "price": float(row["price"]),
                    "category": row["category"].strip().lower(),
                    "stock": int(row["stock"])
                }
                products.append(product)
    except Exception as e:
        print(f"Error loading products: {e}")
    return products

PRODUCTS = load_products()

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

    results = []

    if query:
        results = [p for p in PRODUCTS if query in p['name'] or query in p['description']]
    elif category:
        results = [p for p in PRODUCTS if p['category'] == category.lower()]

    return jsonify(results)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)