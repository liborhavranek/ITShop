from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, template_folder='templates/admin')


@admin.route('/admin')
def product():
    return render_template('admin.html')