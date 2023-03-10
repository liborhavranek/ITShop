from flask import Blueprint, render_template, request, flash, redirect
from .models import Costumer
from . import db
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
auth = Blueprint('auth', __name__, template_folder='templates/authenticates')



@auth.route('/auth')
def authenticate():
    return render_template('auth.html')



@auth.route('/register', methods=['GET', 'POST'])
def register():
    at_sign = '@'
    if request.method == 'POST':
        # ______________user_____________________
        username= request.form.get("username")
        email= request.form.get("email")
        phone_code = request.form.get("phone_code")
        phone = request.form.get("phone")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        #____________fakturacni udaje______________
        faktura_first_name = request.form.get("faktura_first_name")
        faktura_last_name = request.form.get("faktura_last_name")
        faktura_city = request.form.get("faktura_city")
        faktura_street = request.form.get("faktura_street")
        faktura_zipcode = request.form.get("faktura_zipcode")
        
        #_____________dodaci udaje ___________________
        dodej_first_name = request.form.get("dodej_first_name")
        dodej_last_name = request.form.get("dodej_last_name")
        dodej_company = request.form.get("dodej_company")
        dodej_city = request.form.get("dodej_city")
        dodej_street = request.form.get("dodej_street")
        dodej_zipcode = request.form.get("dodej_zipcode")
        dodej_info = request.form.get("dodej_info")
        dodej_phone_code = request.form.get('dodej_phone_code')
        dodej_phone = request.form.get("dodej_phone")
        
        #_____________firemni udaje ______________________
        firma_ico = request.form.get("firma_ico")
        firma_dic = request.form.get("firma_dic")
        firma_bank_acc = request.form.get("firma_bank_acc")
        firma_bank_number = request.form.get("firma_bank_number")
        firma_spec_symbol = request.form.get("firma_spec_symbol")

        
        email_exist = Costumer.query.filter_by(email=email).first()
        costumer_exist = Costumer.query.filter_by(username=username).first()
        if email_exist:
            flash('Tento email je ji?? zaregistrovan??', category='error')
        elif at_sign not in email:
            flash('Email mus?? m??t zavin????', category='error')
        elif costumer_exist:
            flash('Toto p??ihla??ovac?? jm??no je ji?? pou??ito.', category='error')
        elif password1 != password2:
            flash('Heslo a potvrzen?? hesla se mus?? shodovat.', category='error')
        elif len(username) < 6:
            flash('P??ihla??ovac?? jm??no mus?? b??t del???? ne?? 5 znak??.', category='error')
        elif len(password1) < 8:
            flash('Heslo mus?? b??t dlouh?? alespo?? 8 znak??.', category='error')
        elif len(email) < 10:
            flash('Tento email nelze pou????t', category='error')
        elif len(phone) != 9:
            flash("telefonn?? ????slo mus?? m??t 9 ????sel", category='error')
        elif len(faktura_first_name) == 1 or len(faktura_first_name) == 2:
            flash('jm??no mus?? m??t alespo?? t??i znaky', category='error')
        elif len(faktura_last_name) == 1:
            flash('P????jmen?? mus?? m??t alespo?? dva znaky', category='error')
        elif len(faktura_city) == 1:
            flash('M??sto mus?? b??t dlouh?? alespo?? dva znaky', category='error')
        elif len(faktura_street) == 1:
            flash('N??zev ulice mus?? b??t dlouh?? alespo?? dvaznaky', category='error')
        elif len(faktura_zipcode) > 0 and len(faktura_zipcode) < 5:
            flash('PS?? mus?? m??t 5 znak??', category='error')
        elif len(dodej_first_name) == 1 or len(dodej_first_name) == 2:
            flash('jm??no mus?? m??t alespo?? t??i znaky', category='error')
        elif len(dodej_last_name) == 1:
            flash('P????jmen?? mus?? m??t alespo?? dva znaky', category='error')
        elif len(dodej_company) == 1:
            flash('Jm??no firmy mus?? m??t alespo?? dva znaky', category='error')
        elif len(dodej_city) == 1:
            flash('M??sto mus?? b??t dlouh?? alespo?? dva znaky', category='error')
        elif len(dodej_street) == 1:
            flash('N??zev ulice mus?? b??t dlouh?? alespo?? dvaznaky', category='error')
        elif len(dodej_zipcode) > 0 and len(dodej_zipcode) < 5:
            flash('PS?? mus?? m??t 5 znak??', category='error')
        elif len(dodej_info) == 1:
            flash('N??zev ulice mus?? b??t dlouh?? alespo?? dvaznaky', category='error')
        elif len(dodej_phone) > 0 and len(dodej_phone) < 9:
            flash("telefonn?? ????slo mus?? m??t 9 ????sel", category='error')
        elif len(firma_ico) > 0 and len(firma_ico) < 8:
            flash("I??O mus?? b??t dlouh?? 8 ????sel", category='error')
        elif len(firma_dic) > 0 and len(firma_dic) < 10:
            flash("DI?? mus?? b??t dlouh?? alespo?? 10 znak??", category='error')
        elif len(firma_bank_acc) > 0 and len(firma_bank_acc) < 6:
            flash("Bankovn?? ????slo mus?? m??t alespo?? 6 ????sel", category='error')
        elif len(firma_bank_acc) > 0 and len(firma_bank_acc) < 4:
            flash("??islo baky mus?? m??t 4 ????sla", category='error')
        else:
            new_costumer = Costumer(email=email,
                                    username=username,
                                    phone_code=phone_code,
                                    phone=phone,
                                    faktura_first_name=faktura_first_name,
                                    faktura_last_name=faktura_last_name,
                                    faktura_city=faktura_city,
                                    faktura_street = faktura_street,
                                    faktura_zipcode = faktura_zipcode,
                                    dodej_first_name = dodej_first_name,
                                    dodej_last_name = dodej_last_name,
                                    dodej_company = dodej_company,
                                    dodej_city = dodej_city,
                                    dodej_street = dodej_street,
                                    dodej_zipcode = dodej_zipcode,
                                    dodej_info = dodej_info,
                                    dodej_phone = dodej_phone,
                                    dodej_phone_code =dodej_phone_code,
                                    firma_ico = firma_ico,
                                    firma_dic = firma_dic,
                                    firma_bank_acc = firma_bank_acc,
                                    firma_bank_number = firma_bank_number,
                                    firma_spec_symbol = firma_spec_symbol,
                                    password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_costumer)
            db.session.commit()
            login_user(new_costumer, remember=True)
            flash('Profil byl ??sp????n?? vytvo??en.', category='success')
            return render_template('login.html', costumer=current_user)
        
    return render_template('register.html', costumer=current_user)





@auth.route('/check-email', methods=['POST'])
def check_email():
    email = request.form['email']
    user = Costumer.query.filter_by(email=email).first()
    if user:
        return 'taken'
    else:
        return 'available'
    
    
@auth.route('/check-username', methods=['POST'])
def check_username():
    username = request.form['username']
    user = Costumer.query.filter_by(username=username).first()
    if user:
        return 'taken'
    else:
        return 'available'




@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        print(email)
        print(password)
        costumer = Costumer.query.filter_by(email=email).first()
        if costumer:
            if check_password_hash(costumer.password, password):
                flash("??sp????n?? jsi se p??ihl??sil", category='success')
                login_user(costumer, remember=True)
                return render_template("index.html", costumer=current_user)
            else:
                flash('Zadal jsi nespr??vn?? heslo', category='error')
        else:
            flash('Email neexistuje', category='error')

    return render_template("login.html", costumer=current_user)



@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("products")