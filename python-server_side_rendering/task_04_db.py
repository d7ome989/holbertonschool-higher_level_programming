#!/usr/bin/python3
"""Flask application displaying products from JSON, CSV, or SQLite DB."""
import csv
import json
import os
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def create_database():
    """Create and populate the SQLite database if not already initialized."""
    db_path = os.path.join(BASE_DIR, 'products.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()


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


def read_sql_products():
    """Fetch products from the SQLite database."""
    db_path = os.path.join(BASE_DIR, 'products.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        }
        for row in rows
    ]


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
    """Display products based on source (json/csv/sql) and optional id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            data = read_json_products()
        elif source == 'csv':
            data = read_csv_products()
        elif source == 'sql':
            data = read_sql_products()
        else:
            return render_template('product_display.html',
                                   error='Wrong source')
    except sqlite3.Error as e:
        return render_template('product_display.html',
                               error=f'Database error: {e}')

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
    create_database()
    app.run(debug=True, port=5000)
