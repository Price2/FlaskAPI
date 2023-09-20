from flask_sqlalchemy import SQLAlchemy
from db import db
from sqlalchemy_serializer import SerializerMixin



class Category(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    products = db.relationship('Product', back_populates='category', lazy=True)


    serialize_rules = ('-products.category',)  # Exclude products' category from serialization

class Product(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    imgURL = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', back_populates='products')

    serialize_rules = ('-category.products',)  # Exclude category of products from serialization