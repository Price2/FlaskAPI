from flask import Blueprint, request, jsonify
from db import db
from models import Product


product_bp = Blueprint('product_bp', __name__, url_prefix='/api/products')

@product_bp.route('/', methods=['GET'])
def get_products():
    name = request.args.get('name')
    price = request.args.get('price', type=int)
    quantity = request.args.get('quantity', type=int)
    category_id = request.args.get('category_id', type=int)

    query = Product.query

    if name:
        query = query.filter_by(name=name)
    if price is not None:
        query = query.filter_by(price=price)
    if quantity is not None:
        query = query.filter_by(quantity=quantity)
    if category_id is not None:
        query = query.filter_by(category_id=category_id)

    results = query.all()
    serialized_results = [product.to_dict() for product in results]
    return jsonify({"success": True, "results": serialized_results})

@product_bp.route('/<int:id>', methods=['GET'])
def product_by_id(id):
    product = Product.query.get(id)
    if product:
        return jsonify({'success': True, 'results': product.to_dict()})
    else:
        return jsonify({"success": False, "results": {}, "message": f"No product with id={id}"}), 404

@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.json
    try:
        new_product = Product(
            name=data['name'],
            price=data['price'],
            quantity=data['quantity'],
            imgURL=data.get('imgURL'),
            category_id=data['category_id']
        )
        db.session.add(new_product)
        db.session.commit()
        db.session.refresh(new_product)
        return jsonify({"success": True, "results": new_product.to_dict()}), 201
    except Exception as error:
        return jsonify({"success": False, "results": {}, "message": "An error occurred while creating the product"}), 400

@product_bp.route('/api/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    if product:
        data = request.json
        product.name = data['name']
        product.price = data['price']
        product.quantity = data['quantity']
        product.imgURL = data.get('imgURL')
        product.category_id = data['category_id']
        try:
            db.session.commit()
            db.session.refresh(product)
            return jsonify({"success": True, "results": product.to_dict()})
        except Exception as error:
            return jsonify({"success": False, "results": {}, "message": "An error occurred while updating the product"}), 400
    else:
        return jsonify({"success": False, "results": {}, "message": f"No product with id={id}"}), 404

