from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    """Reads data from products.json"""
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    """Reads data from products.csv and converts it to a list of dictionaries"""
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products_list = []

    # Source Loading
    if source == 'json':
        try:
            products_list = read_json()
        except FileNotFoundError:
            return render_template('product_display.html', error="JSON file not found")
    elif source == 'csv':
        try:
            products_list = read_csv()
        except FileNotFoundError:
            return render_template('product_display.html', error="CSV file not found")
    else:
        return render_template('product_display.html', error="Wrong source")

    # ID Filtering
    if product_id:
        try:
            p_id = int(product_id)
            # Filter the list where item['id'] matches the requested id
            products_list = [p for p in products_list if p['id'] == p_id]
            
            if not products_list:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            # If product_id is not an integer
            return render_template('product_display.html', error="Product not found")

    # Render Success
    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
