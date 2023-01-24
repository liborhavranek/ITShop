from flask import Blueprint, render_template

products = Blueprint('products', __name__, template_folder='templates/products')


@products.route('/products')
def product():
    return render_template('products.html')