
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder='templates/authenticates')



@auth.route('/auth')
def authenticate():
    return render_template('auth.html')