import csv
import os

def load_products():
    """
    Loads product data from products.csv
    Returns list of products or empty list if file not found
    """
    products = []
    try:
        with open('products.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    product = {
                        "id": int(row["id"]),
                        "name": row["name"].strip().lower(),
                        "description": row["description"].strip().lower(),
                        "price": float(row["price"]),
                        "category": row["category"].strip().lower(),  # Make lowercase
                        "stock": int(row["stock"])
                    }
                    products.append(product)
                except Exception as e:
                    print(f"⚠️ Skipping row due to error: {e}")
        print("✅ Successfully loaded products from CSV.")
    except FileNotFoundError:
        print("❌ Error: products.csv file not found.")
    return products


def find_products(products, query):
    """
    Search products based on user query (case-insensitive)
    """
    query = query.strip().lower()
    results = []

    # Match by category
    categories = {"electronics", "books", "textiles"}
    if query in categories:
        results = [p for p in products if p['category'] == query]
    else:
        results = [p for p in products if query in p['name'] or query in p['description']]

    return results


def main():
    print("🛍️ Welcome to the E-commerce Chatbot Demo")
    print("Type 'exit' to quit.\n")

    products = load_products()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['exit', 'quit']:
            print("Bot: Goodbye!")
            break

        matched_products = find_products(products, user_input)

        if matched_products:
            print(f"Bot: Found {len(matched_products)} product(s):")
            for p in matched_products[:5]:
                print(f"- {p['name'].title()} | ₹{p['price']} | Stock: {p['stock']}")
        else:
            print("Bot: No matching products found.")


if __name__ == "__main__":
    main()