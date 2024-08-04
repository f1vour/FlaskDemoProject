from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User, Product, Order, OrderItem

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    # Add product to cart (session-based or database)
    return redirect(url_for('index'))

# Add routes for user registration, login, and order processing as needed.
