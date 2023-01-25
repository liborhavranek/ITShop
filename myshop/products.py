from flask import Blueprint, render_template, request, flash, redirect, get_flashed_messages, jsonify

products = Blueprint('products', __name__, template_folder='templates/products')
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from .models import Brand
from . import db

@products.route('/products')
def product():
    return render_template('products.html')


# Pokud přidám kategorii nebo budu psát kód s podmínkami např jako mám tady musí být delší 
# než dva znaky tak můžu každou podmínku vypsat a pod ní vrátit jsonify, kód tak bude 
# velmi dlouhý u více podmínek proto jsem si vytvořil funkci handle_response a proto můžu 
# pod podmínkou flashnout zprávu a přivolat funkci handle_responze, kód tak bude kratší při více
# podmínkách

def handle_response(data={}):
    return jsonify({
        'flash_message': get_flashed_messages(with_categories=True)
    } if not data else data)







@products.route('/addbrand', methods=['GET', 'POST'])
@login_required
def addbrand():
    brands = Brand.query.all() 
    if request.method == 'POST':
        brand = request.form.get("brand").title()
        if len(brand) < 3:
            flash("Značka musí mít alespoň tři znaky!", category="danger")
            return handle_response()
        existing_brand = Brand.query.filter_by(brand=brand).first()
        if existing_brand:
            flash("Značka už existuje !", category="danger")
            return handle_response()
        else:
            new_brand = Brand(brand=brand, date_created=datetime.now())
            db.session.add(new_brand)
            db.session.commit()
            flash("Značka byla přidána", category="success")
            return handle_response(data={
                'flash_message': get_flashed_messages(with_categories=True),
                'brand': new_brand.brand,
                'id': new_brand.id,
                'date_created': new_brand.date_created
            })
    return render_template('addbrand.html', brands=brands)



@products.route('/editbrand/<int:id>', methods=['GET','POST'])
@login_required
def editbrand(id):
    brand = Brand.query.filter_by(id=id).first()
    if request.method == 'POST':
        new_brand = request.form.get("edit_brand").title()
        if len(new_brand) < 3:
            flash("Značka musí mít minimálně 3 znaky!", category="danger")
            return handle_response()
        existing_brand = Brand.query.filter_by(brand=new_brand).first()
        if existing_brand:
            flash("Značka už existuje!", category="danger")
            return handle_response()
        else:
            brand.brand = new_brand
            db.session.commit()
            flash('Značka byla upravena.', category='success')
            return handle_response(data={
            'flash_message': get_flashed_messages(with_categories=True),
            'brand': brand.brand,
            })
    return render_template('editbrand.html', brand=brand)