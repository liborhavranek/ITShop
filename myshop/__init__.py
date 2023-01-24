from flask import Flask
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from os import path


DB_NAME = "myshop.db"
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    create_database(app)
    
    
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
  )
} 
    assets.register(bundles)
    
    return app
    

def create_database(app):
    if not path.exists('shop/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')