from flask import Blueprint, render_template, request, flash, redirect, get_flashed_messages, jsonify

products = Blueprint('products', __name__, template_folder='templates/products')
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from .models import Brand, Category, Color, Product
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
                'date_created': new_brand.date_created,
                'date_edited': new_brand.date_edited,
                'edited': new_brand.edited,
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
            brand.date_edited = datetime.now()
            brand.edited = True
            db.session.commit()
            flash('Značka byla upravena.', category='success')
            return handle_response(data={
            'flash_message': get_flashed_messages(with_categories=True),
            'brand': brand.brand,
            })
    return render_template('editbrand.html', brand=brand)



@products.route('/deletebrand/<int:id>', methods=['DELETE'])
@login_required
def deletebrand(id):
    brand = Brand.query.filter_by(id=id).first()
    db.session.delete(brand)
    db.session.commit()
    return jsonify({'message': 'Značka byla smazána'})






@products.route('/addcategory', methods=['GET', 'POST'])
@login_required
def addcategory():
    categories = Category.query.all() 
    if request.method == 'POST':
        category = request.form.get("category").title()
        if len(category) < 3:
            flash("Kategorie musí mít minimálně 3 znaky", category="danger")
            return handle_response()
        existing_category = Category.query.filter_by(category=category).first()
        if existing_category:
            flash("Kategorie už existuje !", category="danger")
            return handle_response()
        else:
            new_category = Category(category=category, date_created=datetime.now())
            db.session.add(new_category)
            db.session.commit()
            flash("Kategorie byla přidána", category="success")
            return handle_response(data={
                'flash_message': get_flashed_messages(with_categories=True),
                'category': new_category.category,
                'id': new_category.id,
                'date_created': new_category.date_created,
                'date_edited': new_category.date_edited,
                'edited': new_category.edited,
            })
    return render_template('addcategory.html', categories=categories)



@products.route('/editcategory/<int:id>', methods=['GET','POST'])
@login_required
def editcategory(id):
    category = Category.query.filter_by(id=id).first()
    if request.method == 'POST':
        new_category = request.form.get("edit_category").title()
        if len(new_category) < 3:
            flash("Kategorie musí mít minimálně 3 znaky!", category="danger")
            return handle_response()
        existing_category = Category.query.filter_by(category=new_category).first()
        if existing_category:
            flash("Kategorie už existuje!", category="danger")
            return handle_response()
        else:
            category.category = new_category
            category.date_edited = datetime.now()
            category.edited = True
            db.session.commit()
            flash('Kategorie byla editována.', category='success')
            return handle_response(data={
            'flash_message': get_flashed_messages(with_categories=True),
            'category': category.category,
            })
    return render_template('editcategory.html', category=category)



@products.route('/deletecategory/<int:id>', methods=['DELETE'])
@login_required
def deletecategory(id):
    category = Category.query.filter_by(id=id).first()
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Kategorie byla smazána'})



@products.route('/addcolor', methods=['GET', 'POST'])
@login_required
def addcolor():
    colors = Color.query.all() 
    if request.method == 'POST':
        color = request.form.get("color").title()
        if len(color) < 3:
            flash("Barva musí mít minimálně 3 znaky", category="danger")
            return handle_response()
        existing_color = Color.query.filter_by(color=color).first()
        if existing_color:
            flash("Barva už existuje !", category="danger")
            return handle_response()
        else:
            new_color = Color(color=color, date_created=datetime.now())
            db.session.add(new_color)
            db.session.commit()
            flash("Barva byla přidána", category="success")
            return handle_response(data={
                'flash_message': get_flashed_messages(with_categories=True),
                'color': new_color.color,
                'id': new_color.id,
                'date_created': new_color.date_created,
                'date_edited': new_color.date_edited,
                'edited': new_color.edited,
            })
    return render_template('addcolor.html', colors=colors)



@products.route('/editcolor/<int:id>', methods=['GET','POST'])
@login_required
def editcolor(id):
    color = Color.query.filter_by(id=id).first()
    if request.method == 'POST':
        new_color = request.form.get("edit_color").title()
        if len(new_color) < 3:
            flash("Barva musí mít minimálně 3 znaky!", category="danger")
            return handle_response()
        existing_color = Color.query.filter_by(color=new_color).first()
        if existing_color:
            flash("Barva už existuje!", category="danger")
            return handle_response()
        else:
            color.color = new_color
            color.date_edited = datetime.now()
            color.edited = True
            db.session.commit()
            flash('Barva byla editována.', category='success')
            return handle_response(data={
            'flash_message': get_flashed_messages(with_categories=True),
            'color': color.color,
            })
    return render_template('editcolor.html', color=color)
  
  
  
@products.route('/deletecolor/<int:id>', methods=['DELETE'])
@login_required
def deletecolor(id):
    color = Color.query.filter_by(id=id).first()
    db.session.delete(color)
    db.session.commit()
    return jsonify({'message': 'Barva byla smazána'})



@products.route('/addproduct/', methods=['GET', 'POST'])
@login_required
def addproduct():
    brands = Brand.query.all()
    categories = Category.query.all()
    colors = Color.query.all()
    products = Product.query.all() 
    if request.method == 'POST':
        product = request.form.get("product").title()
        price = request.form.get('price')
        discount = request.form.get('discount')
        stock = request.form.get('stock')
        size = request.form.get('size')
        description = request.form.get('description')
        category_id = request.form.get('category')
        color_id = request.form.get('color')
        brand_id = request.form.get('brand')
        
        product_color = Color.query.filter_by(id=color_id).first()
        color = product_color.color
        
        product_brand = Brand.query.filter_by(id=brand_id).first()
        brand = product_brand.brand
        
        product_category = Category.query.filter_by(id=category_id).first()
        category = product_category.category
        
        
        existing_product = Product.query.filter_by(product=product).first()
        int_price = int(price)
        if existing_product:
            flash("Produkt už existuje !", category="danger")
        if len(product) < 3:
            flash("Produkt musí mít minimálně 3 znaky", category="danger")
        elif int_price < 1:
            flash("Cena musí být alespoň jedna koruna", category='danger')
        else:
            
            new_product= Product(product=product,
                                 price=price,
                                 discount=discount,
                                 stock=stock,
                                 size=size,
                                 description=description,
                                 pub_date=datetime.now(),
                                 category_id=category_id,
                                 color_id=color_id,
                                 brand_id=brand_id,
                                 )
            db.session.add(new_product)
            db.session.commit()
            flash('Produkt byl přidán', category='success')
            return handle_response(data={
                'flash_message': get_flashed_messages(with_categories=True),
                'id': new_product.id,
                'product': new_product.product,
                'price': new_product.price,
                'discount': new_product.discount,
                'stock': new_product.stock,
                'size': new_product.size,
                'category_id': new_product.category_id,
                'color_id': new_product.color_id,
                'brand_id':new_product.brand_id,
                'color': color,
                'brand': brand,
                'category':category,
            })
    return render_template('addproduct.html', products=products, brands=brands, categories=categories, colors=colors)



@products.route('/check-product-name', methods=['POST'])
def check_product_name():
    product = request.form['product']
    name = Product.query.filter_by(product=product).first()
    if name:
        return 'taken'
    else:
        return 'available'
    


# @products.route('/editproduct/<int:id>', methods=['GET', 'POST'])
# @login_required
# def editproduct(id):
#     products = Product.query.filter_by(id=id).first()
#     if request.method == 'POST':
#         product = request.form.get("product").title()
#         price = request.form.get('price')
#         discount = request.form.get('discount')
#         stock = request.form.get('stock')
#         size = request.form.get('size')
#         description = request.form.get('description')
#         category_id = request.form.get('category')
#         color_id = request.form.get('category')
#         brand_id = request.form.get('brand')
#         existing_product = Product.query.filter_by(product=product).first()
#         int_price = int(price)
#         if existing_product:
#             flash("Produkt už existuje !", category="danger")
#         if len(product) < 3:
#             flash("Produkt musí mít minimálně 3 znaky", category="danger")
#         elif int_price < 1:
#             flash("Cena musí být alespoň jedna koruna", category='danger')
#         else:
            
#             flash('Produkt byl přidán', category='success')
#             return handle_response(data={
#                 'flash_message': get_flashed_messages(with_categories=True),
#                 'id': new_product.id,
#                 'product': new_product.product,
#                 'price': new_product.price,
#                 'discount': new_product.discount,
#                 'stock': new_product.stock,
#                 'size': new_product.size,
#                 'category_id': new_product.category_id,
#                 'color_id': new_product.color_id,
#             })
#     return render_template('addproduct.html', products=products, brands=brands, categories=categories, colors=colors)