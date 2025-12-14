import sqlite3
from flask import Flask, render_template, request
import csv
import json
import os

app = Flask(__name__)

JSON_FILE = 'products.json'
CSV_FILE = 'products.csv'
DB_FILE = 'products.db'

def get_product_data_from_json():
    """Reads product data from the JSON file."""
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
        return []

def get_product_data_from_csv():
    """Reads product data from the CSV file."""
    if not os.path.exists(CSV_FILE):
        return []
    try:
        products = []
        with open(CSV_FILE, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    products.append(row)
                except (ValueError, KeyError) as e:
                    print(f"Error parsing CSV row: {row} - {e}")
        return products
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

def initialize_database(initial_data):
    """
    Creates the database table and inserts data if not present.
    It takes a list of products to initially populate the DB.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    existing_ids = set()
    cursor.execute("SELECT id FROM Products")
    for row in cursor.fetchall():
        existing_ids.add(row[0])

    for product in initial_data:
        if product['id'] not in existing_ids:
            try:
                cursor.execute("INSERT OR IGNORE INTO Products (id, name, category, price) VALUES (?, ?, ?, ?)",
                               (product['id'], product['name'], product['category'], product['price']))
            except KeyError as e:
                print(f"Skipping product due to missing key: {product} - {e}")

    conn.commit()
    conn.close()

def get_products_from_db():
    """Fetches all products from the SQLite database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        products = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

# --- Flask Routes ---
@app.route('/products')
def products():
    source = request.args.get('source')
    data = []
    error = None

    if source == 'json':
        data = get_product_data_from_json()
        if not data:
            error = "JSON data not found."
    elif source == 'csv':
        data = get_product_data_from_csv()
        if not data: 
            error = "CSV data not found."
    elif source == 'sql':
        data = get_products_from_db()
        if data is None:
            error = "Error fetching data from database."
    else:
        error = "Wrong source"

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    initial_product_seed = get_product_data_from_json()

    if not initial_product_seed:
        initial_product_seed = [
            {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
            {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
        ]
        with open(JSON_FILE, 'w') as f:
            json.dump(initial_product_seed, f, indent=4)
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'name', 'category', 'price'])
            writer.writeheader()
            writer.writerows(initial_product_seed)


    initialize_database(initial_product_seed)


    app.run(debug=True)