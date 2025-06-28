from flask import Blueprint, render_template, request, redirect, url_for
from .models import get_all_products, add_product

main = Blueprint('main', __name__)

@main.route('/')
def index():
    products = get_all_products()
    return render_template('index.html', products=products)

@main.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        image = request.form['image']
        add_product({'name': name, 'price': price, 'image': image})
        return redirect(url_for('main.admin'))
    return render_template('admin.html')
