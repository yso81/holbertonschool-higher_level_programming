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
def items_index():
    with open('items.json') as f:
        data = json.load(f)
    # Pass the whole dictionary as 'all_lists'
    return render_template('items.html', all_lists=data)

# Show a SPECIFIC list
@app.route('/items/<category>')
def items_category(category):
    with open('items.json') as f:
        data = json.load(f)
    
    selected_items = data.get(category)
    
    if selected_items is None:
        return f"Category '{category}' not found.", 404

    # Pass specific list as 'items'
    return render_template('items.html', items=selected_items, title=category)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
