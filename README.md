🛒 E-commerce Chatbot – UplYft Case Study
A simple yet effective e-commerce chatbot built using Flask (Python) and HTML/CSS/JavaScript , with mock product data from a CSV file. This chatbot allows users to search for products by name or category, and displays results dynamically in a conversational interface.

🧾 Features

✅ Responsive frontend UI
💬 Product search via name or category
📱 Category buttons: Electronics, Books, Textiles
⏰ Typing indicator and timestamps
🗃️ Stores conversation history using localStorage
🎯 Works entirely offline after setup

🧰 Requirements

Before you begin, ensure you have the following installed:
>Python
3.10+

>Flask
Latest

>SQLite (optional)
For persistent database

>pip
Included with Python

>git (optional)
For version control

🔁 You can skip the database part and run it purely from CSV if needed. 

📦 Folder Structure
Uplyft/
├── backend/
│   ├── app.py                # Flask API server
│   ├── database.py             # DB schema creation
│   ├── seed_data.py            # Seeding script
│   └── static/
│       ├── index.html          # Chatbot UI
│       └── style.css           # CSS styling (embedded in HTML)
│
├── instance/
│   └── chatbot.db              # Auto-generated SQLite DB (if using database)
│
├── products.csv               # Mock product data (CSV)
└── README.md                  # This file

🛠️ Setup Instructions

1. Clone or Download the Repository
git clone https://github.com/your-username/uplyft-chatbot.git 
cd uplyft-chatbot/backend


2. Create and Activate Virtual Environment
python -m venv .venv
.\.venv\Scripts\activate      # Windows
source .venv/bin/activate     # Mac/Linux


3. Install Dependencies
pip install Flask flask-cors
✅ No other dependencies are required if running without database (CSV-only mode) 



🚀 Running the Chatbot
Option A: With Database
1. Initialize the Database Schema
python database.py

2. Seed the Database with Products
python seed_data.py

3. Start Flask Server
python app.py

4. Open in Browser
http://localhost:5000/

You’ll see the chatbot interface. Try typing:

"books"
"electronics"
"t-shirts"
The bot will respond with matching products from the database.

Option B: Without Database (Direct CSV Reading)
If you're facing issues with SQLite or want a simpler setup:

1. Update app.py to Read Directly from CSV
Use this code snippet to replace the /api/products route:

python

import csv

PRODUCTS = []

def load_products():
    global PRODUCTS
    PRODUCTS.clear()
    with open('static/products.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                product = {
                    "id": int(row["id"]),
                    "name": row["name"].strip().lower(),
                    "description": row["description"].strip().lower(),
                    "price": float(row["price"]),
                    "category": row["category"].strip().lower(),
                    "stock": int(row["stock"])
                }
                PRODUCTS.append(product)
            except Exception as e:
                print(f"⚠️ Skipping row due to error: {e}")
    print(f"✅ Loaded {len(PRODUCTS)} products")

@app.route('/api/products', methods=['GET'])
def search_products():
    query = request.args.get('q', '').strip().lower()
    category = request.args.get('category', None)

    if not query and not category:
        return jsonify({"error": "Either 'q' or 'category' must be provided."}), 400

    matches = []
    for p in PRODUCTS:
        if category and p['category'] == category.lower():
            matches.append(p)
        elif query and (query in p['name'] or query in p['description']):
            matches.append(p)

    return jsonify(matches)


2. Run Flask App
cd backend
python app.py

3. Visit Chatbot
http://localhost:5000/

Type queries like:

"books"
"smartphones"
"under 20 dollars" (if supported)
And the bot will respond with matching products directly from the CSV.

🧪 Sample Queries

"books": Returns books from the dataset
"electronics": Shows electronics
"cotton t-shirt": Matches specific product
"show me under 100": Should return affordable items

🧑‍💻 Frontend Interaction

Type a message into the input box and click Send
Or click on category buttons to filter products
The chatbot will display results in styled cards
Conversations are saved in localStorage across sessions

🧩 Technical Details

Backend: Python + Flask
Frontend: Vanilla JS + HTML + CSS
Data Source: products.csv (100+ mock entries)
Optional: SQLite database (chatbot.db) for persistent storage

