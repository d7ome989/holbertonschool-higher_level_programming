#!/usr/bin/python3
"""Flask application rendering dynamic items from a JSON file."""
import json
import os
from flask import Flask, render_template

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the items list page from items.json."""
    items_path = os.path.join(BASE_DIR, 'items.json')
    try:
        with open(items_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except (OSError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
