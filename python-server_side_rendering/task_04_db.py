import sqlite3
from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute("SELECT COUNT(*) FROM Products WHERE id IN (1, 2, 3)")
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99),
            (3, 'Jarvis', 'Electronics', 1299.99)
        ''')
        conn.commit()
    conn.close()

def get_products_from_db():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        products = []
        for row in cursor.fetchall():
            products.append({"id": row[0], "name": row[1], "category": row[2], "price": row[3]})
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    data = []
    error = None

    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            error = "JSON file not found."
        except json.JSONDecodeError:
            error = "Error decoding JSON."
    elif source == 'csv':
        try:
            with open('products.csv', 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    data.append(row)
        except FileNotFoundError:
            error = "CSV file not found."
        except Exception as e:
            error = f"Error reading CSV: {e}"
    elif source == 'sql':
        data = get_products_from_db()
        if data is None:
            error = "Error fetching data from database."
    else:
        error = "Wrong source"

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    create_database()
    with open('products.json', 'w') as f:
        json.dump([
            {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
            {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99},
            {"id": 3, "name": "Jarvis", "category": "Electronics", "price": 1299.99}
        ], f)
    with open('products.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'name', 'category', 'price'])
        writer.writerow([1, 'Laptop', 'Electronics', 799.99])
        writer.writerow([2, 'Coffee Mug', 'Home Goods', 15.99])
        writer.writerow([3, 'Jarvis', 'Electronics', 1299.99])

    app.run(debug=True)
