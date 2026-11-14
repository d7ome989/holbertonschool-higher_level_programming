#!/usr/bin/python3
"""Flask application displaying products from JSON or CSV files."""
import csv
import json
import os
from flask import Flask, render_template, request

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_json_products():
    """Read and parse products from products.json."""
    filepath = os.path.join(BASE_DIR, 'products.json')
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def read_csv_products():
    """Read and parse products from products.csv."""
    filepath = os.path.join(BASE_DIR, 'products.csv')
    products = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


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
    """Render the items list page."""
    items_path = os.path.join(BASE_DIR, 'items.json')
    try:
        with open(items_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except (OSError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    """Display products based on source (json/csv) and optional id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json_products()
    elif source == 'csv':
        data = read_csv_products()
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        try:
            target_id = int(product_id)
            data = [p for p in data if int(p['id']) == target_id]
        except ValueError:
            data = []

        if not data:
            return render_template('product_display.html',
                                   error='Product not found')

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
