from flask import Blueprint, render_template, request, flash
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
            flash('Tento email je již zaregistrovaný', category='error')
        elif at_sign not in email:
            flash('Email musí mít zavináč', category='error')
        elif costumer_exist:
            flash('Toto přihlašovací jméno je již použito.', category='error')
        elif password1 != password2:
            flash('Heslo a potvrzení hesla se musí shodovat.', category='error')
        elif len(username) < 6:
            flash('Přihlašovací jméno musí být delší než 5 znaků.', category='error')
        elif len(password1) < 8:
            flash('Heslo musí být dlouhé alespoň 8 znaků.', category='error')
        elif len(email) < 10:
            flash('Tento email nelze použít', category='error')
        elif len(phone) != 9:
            flash("telefonní číslo musí mít 9 čísel", category='error')
        elif len(faktura_first_name) == 1 or len(faktura_first_name) == 2:
            flash('jméno musí mít alespoň tři znaky', category='error')
        elif len(faktura_last_name) == 1:
            flash('Příjmení musí mít alespoň dva znaky', category='error')
        elif len(faktura_city) == 1:
            flash('Město musí být dlouhé alespoň dva znaky', category='error')
        elif len(faktura_street) == 1:
            flash('Název ulice musí být dlouhý alespoň dvaznaky', category='error')
        elif len(faktura_zipcode) > 0 and len(faktura_zipcode) < 5:
            flash('PSČ musí mít 5 znaků', category='error')
        elif len(dodej_first_name) == 1 or len(dodej_first_name) == 2:
            flash('jméno musí mít alespoň tři znaky', category='error')
        elif len(dodej_last_name) == 1:
            flash('Příjmení musí mít alespoň dva znaky', category='error')
        elif len(dodej_company) == 1:
            flash('Jméno firmy musí mít alespoň dva znaky', category='error')
        elif len(dodej_city) == 1:
            flash('Město musí být dlouhé alespoň dva znaky', category='error')
        elif len(dodej_street) == 1:
            flash('Název ulice musí být dlouhý alespoň dvaznaky', category='error')
        elif len(dodej_zipcode) > 0 and len(dodej_zipcode) < 5:
            flash('PSČ musí mít 5 znaků', category='error')
        elif len(dodej_info) == 1:
            flash('Název ulice musí být dlouhý alespoň dvaznaky', category='error')
        elif len(dodej_phone) > 0 and len(dodej_phone) < 9:
            flash("telefonní číslo musí mít 9 čísel", category='error')
        elif len(firma_ico) > 0 and len(firma_ico) < 8:
            flash("IČO musí být dlouhé 8 čísel", category='error')
        elif len(firma_dic) > 0 and len(firma_dic) < 10:
            flash("DIČ musí být dlouhé alespoň 10 znaků", category='error')
        elif len(firma_bank_acc) > 0 and len(firma_bank_acc) < 6:
            flash("Bankovní číslo musí mít alespoň 6 čísel", category='error')
        elif len(firma_bank_acc) > 0 and len(firma_bank_acc) < 4:
            flash("Čislo baky musí mít 4 čísla", category='error')
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
            flash('Profil byl úspěšně vytvořen.', category='success')
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
