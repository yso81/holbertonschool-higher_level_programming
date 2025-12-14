from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    """Reads data from products.json"""
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    """Reads data from products.csv and converts it to a list of dictionaries"""
    products = []
    with open('products.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
            except (ValueError, KeyError) as e:
                print(f"Skipping CSV row due to parsing error: {row} - {e}")
                continue
    return products

def get_products_from_db():
    """Fetches all products from the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        products = []
        for row in cursor.fetchall():
            products.append(dict(row))
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        if conn:
            conn.close()

# --- Flask Route ---

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products_list = []
    error = None

    if source == 'json':
        try:
            products_list = read_json()
        except FileNotFoundError:
            error = "JSON file not found."
        except json.JSONDecodeError:
            error = "Error decoding JSON file."
    elif source == 'csv':
        try:
            products_list = read_csv()
        except FileNotFoundError:
            error = "CSV file not found."
    elif source == 'sql':
        products_list = get_products_from_db()
        if products_list is None:
            error = "Error fetching data from database."
    else:
        error = "Wrong source"

    if error:
        return render_template('product_display.html', error=error)

    if product_id:
        try:
            p_id = int(product_id)
            products_list = [p for p in products_list if p.get('id') == p_id]
            
            if not products_list:
                error = "Product not found"
        except ValueError:
            error = "Invalid product ID format."
    
    return render_template('product_display.html', products=products_list, error=error)

if __name__ == '__main__':
    
    app.run(debug=True, port=5000)
