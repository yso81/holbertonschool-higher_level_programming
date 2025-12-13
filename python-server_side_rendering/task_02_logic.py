import json
from flask import Flask, render_template

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
        # Open the JSON file
        with open('items.json', 'r') as f:
            data = json.load(f)
        
        # Access the specific list from your JSON
        items_list = data['list_1']
        
        # Pass the list to the template
        return render_template('items.html', items=items_list)
        
    except FileNotFoundError:
        return "items.json file not found. Please check the file location."
    except KeyError as e:
        return f"KeyError: Key {e} not found in JSON file. Check your keys."

if __name__ == '__main__':
    app.run(debug=True, port=5000)
