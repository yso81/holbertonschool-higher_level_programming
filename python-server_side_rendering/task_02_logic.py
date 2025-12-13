from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        # Open and load the JSON file
        with open('items.json', 'r') as f:
            data = json.load(f)
        
        # Extract the list using the key "items" defined in the JSON file
        items_list = data.get('items', [])
        
        # Pass the list to the template
        return render_template('items.html', items=items_list)
        
    except FileNotFoundError:
        return "items.json not found", 404
    except json.JSONDecodeError:
        return "Error decoding JSON", 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)