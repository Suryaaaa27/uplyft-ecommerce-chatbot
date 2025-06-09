This README includes:

-Project overview
-Folder structure
-Setup instructions (local + deployment)
-Technical documentation
-Troubleshooting tips

🛒 E-commerce Chatbot – UplYft Full Stack Intern Case Study
A simple yet functional e-commerce chatbot built using Flask (Python) for backend and HTML/CSS/JavaScript for the frontend. This chatbot allows users to search for products by name or category and displays results in a conversational UI.

🧾 Features
✅ Product search via name or category
💬 Chat-based interaction with typing indicator
📱 Category buttons: Electronics, Books, Textiles
⏰ Timestamps and localStorage support
🔊 Optional voice command support (Web Speech API)
🗃️ Works with or without SQLite database
🌐 Deployed version works on Render/Railway
📋 Clean project structure and detailed documentation

🧰 Technology Stack Used
Backend- Python Flask
Frontend- HTML5, CSS3, Vanilla JavaScript
Data Source- products.csv or optional SQLite (chatbot.db)
Hosting- Render / Railway (via Gunicorn)
API- RESTful /api/products?q=<query>&category=<category>
Tools- Git, GitHub, Web Speech API

📁 Folder Structure
uplyft-chatbot/
│
├── backend/
│   ├── app.py                # Flask server
│   ├── static/
│   │   └── index.html        # Chatbot UI
│   ├── seed_data.py          # CSV → DB seeder
│   └── database.py           # SQLite schema setup
│
├── instance/
│   └── chatbot.db            # Auto-generated SQLite database (optional)
│
├── products.csv              # Mock product data (100+ entries)
├── requirements.txt          # Python dependencies
├── Procfile                  # Deployment start command
└── README.md                 # This file


🛠 Local Setup Instructions
1. Clone the Repository
   git clone https://github.com/Suryaaaa27/uplyft-chatbot.git 
   cd uplyft-chatbot
2. Create and Activate Virtual Environment
   python -m venv .venv
   .\.venv\Scripts\activate     # Windows
   source .venv/bin/activate     # Mac/Linux
3. Install Dependencies
   pip install -r requirements.txt
   
Requirements include: 
Flask
flask-cors
gunicorn (for deployment)

Set Up Database (Optional)
If using SQLite:

a. Create the database schema:
   cd backend
   python ../database.py
b. Seed the database with mock data:
   python ../seed_data.py

🚀 Run Locally
From the backend/ folder:
  python app.py
Then visit:
  http://localhost:5000/

Try these queries:

"electronics"
"books"
"smartphone"
"t-shirt"
You should see matching products returned from the database or CSV.

🌐 Deploy on Render or Railway
1. Push Code to GitHub
2. Create a New Web Service on Render or Railway
   
Use this start command if deploying manually:
cd backend && gunicorn app:app --bind :$PORT

Or use a Procfile at root:
web: cd backend && gunicorn app:app --bind :$PORT

Ensure requirements.txt contains:
Flask==3.0.0
flask-cors==4.0.0
gunicorn==21.2.0


🧪 Sample Queries You Can Try
"show me electronics"
Returns smartphones, headphones, etc.
"books under 20 dollars"
Matches books with price filtering
"textiles"
Shows t-shirts, cotton fabrics, etc.
"cotton"
Returns relevant textile products
"smartphones"
Matches electronics based on name/description

🧑‍💻 Key Code Snippets
✅ Flask API Endpoint (app.py)
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

✅ Chatbot UI (static/index.html)
Includes:

Typing animation
Product cards
Category buttons
Voice input support

🧩 How It Works
User types or uses voice input.
The bot calls /api/products?q=<query> or /api/products?category=<category>
The backend returns JSON product data.
Results are rendered as styled cards in the chat window.

Summary
The UplYft E-commerce Chatbot was developed as part of the Full Stack Intern Case Study. The application allows users to search for products by name or category using either typed or voice-based input. It utilizes Python + Flask for the backend and vanilla HTML/CSS/JS for the frontend.

Objectives
Build a working chatbot interface
Enable product search functionality
Allow filtering by category
Implement voice input capability
Ensure compatibility across local and online environments

Challenges Faced
Resolving path issues when serving static files and databases
Handling case-insensitive product/category matching
Ensuring Gunicorn compatibility on cloud platforms
Fixing deployment errors related to missing packages

How It Was Solved
Used relative paths and environment variables for portability
Added .lower() handling for better UX
Used products.csv as fallback data source
Created a Procfile for production-ready deployment

🚀 Final Notes
This project meets all UplYft Case Study requirements:

✅ Working chatbot UI
✅ Product search and filtering
✅ Modern design and interaction
✅ Clean documentation and setup steps

Screenshots:
![Screenshot 2025-06-08 204513](https://github.com/user-attachments/assets/2fd568a2-337c-47db-b935-b98d1803e649)
![Screenshot 2025-06-08 204451](https://github.com/user-attachments/assets/33776108-ed0b-4280-8a17-46a2c898fc4f)
![Screenshot 2025-06-08 204429](https://github.com/user-attachments/assets/726ca97a-81ef-44b6-bfd0-d8103ea08078)
