from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate

DB_NAME = "myshop.db"
db = SQLAlchemy()

migrate = Migrate()

login_manager = LoginManager()

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    csrf.init_app(app)
    migrate.init_app(app, db,compare_type=True)
    
    
    from .models import Costumer
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return Costumer.query.get(id)
    
    from .admin import admin
    from .products import products
    from .views import views
    from .auth import auth

    app.register_blueprint(admin, url_prefix='/')
    app.register_blueprint(products, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    
    
    assets = Environment(app)
    bundles = {  # define nested Bundle
    'index_style': Bundle(
            'SCSS/index.scss',
            filters='libsass',
            output='Gen/index.css',
  ),
    'register_style': Bundle(
            'SCSS/register.scss',
            filters='libsass',
            output='Gen/register.css',
  ),
  'product_style': Bundle(
            'SCSS/product.scss',
            filters='libsass',
            output='Gen/product.css',
  )
} 
    assets.register(bundles)
    
    return app
    

def create_database(app):
    if not path.exists('myshop/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('table created')
        print('Created Database!')