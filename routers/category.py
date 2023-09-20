# routers/category.py

from flask import Blueprint, request, jsonify
from db import db
from models import Category

category_bp = Blueprint('category_bp', __name__, url_prefix='/api/categories')

@category_bp.route('/', methods=['POST'])
def add_category():
    data = request.json
    name = data.get('name')
    
    if not name:
        return jsonify({"error": "Name is required"}), 400
    
    new_category = Category(name=name)
    db.session.add(new_category)
    db.session.commit()
    db.session.refresh(new_category)
    return jsonify({"success": True, "results": new_category.to_dict()}), 201



@category_bp.route('/', methods=['GET'])
def get_categories():
    id = request.args.get('id')
    name = request.args.get('name')
    
    query = Category.query
    
    if id:
        query = query.filter_by(id=id)
    
    if name:
        query = query.filter_by(name=name)
    
    results = query.all()
    serialized_results = [category.to_dict() for category in results]
    return jsonify({"success": True, "results": serialized_results}), 200
