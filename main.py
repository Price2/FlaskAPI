# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routers.category import category_bp
from routers.product import product_bp
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)


app.register_blueprint(category_bp)
app.register_blueprint(product_bp)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
