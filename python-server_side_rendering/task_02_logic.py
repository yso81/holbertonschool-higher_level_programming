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
    # Open and load the JSON file
    with open('items.json') as f:
        data = json.load(f)
    
    # Choose which list to display
    current_list = data['list_1'] 

    # Pass the list to the template using the variable name 'items'
    return render_template('items.html', items=current_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
