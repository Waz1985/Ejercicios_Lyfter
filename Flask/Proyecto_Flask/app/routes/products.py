from decimal import Decimal, InvalidOperation

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from ..auth import admin_required
from ..cache_utils import PRODUCT_DETAIL_KEY, PRODUCT_LIST_KEY, invalidate_products_cache
from ..extensions import cache, db
from ..models import Product

products_bp = Blueprint("products", __name__)


def _product_payload(data):
    required = ["name", "sku", "price", "stock"]
    missing = [field for field in required if data.get(field) in (None, "")]
    if missing:
        return None, (jsonify({"error": "Missing required fields", "fields": missing}), 400)
    try:
        price = Decimal(str(data["price"]))
        stock = int(data["stock"])
    except (InvalidOperation, ValueError, TypeError):
        return None, (jsonify({"error": "Invalid price or stock"}), 400)
    if price < 0 or stock < 0:
        return None, (jsonify({"error": "Price and stock cannot be negative"}), 400)
    return {
        "name": data["name"],
        "description": data.get("description"),
        "sku": data["sku"],
        "price": price,
        "stock": stock,
        "is_active": bool(data.get("is_active", True)),
    }, None


@products_bp.get("")
@jwt_required()
def list_products():
    cached = cache.get(PRODUCT_LIST_KEY)
    if cached is not None:
        return jsonify(cached)
    products = [product.to_dict() for product in Product.query.filter_by(is_active=True).order_by(Product.id).all()]
    cache.set(PRODUCT_LIST_KEY, products, timeout=120)
    return jsonify(products)


@products_bp.get("/<int:product_id>")
@jwt_required()
def get_product(product_id):
    key = PRODUCT_DETAIL_KEY.format(product_id=product_id)
    cached = cache.get(key)
    if cached is not None:
        return jsonify(cached)
    product = Product.query.get_or_404(product_id)
    payload = product.to_dict()
    cache.set(key, payload, timeout=300)
    return jsonify(payload)


@products_bp.post("")
@admin_required
def create_product():
    data = request.get_json() or {}
    payload, error = _product_payload(data)
    if error:
        return error
    if Product.query.filter_by(sku=payload["sku"]).first():
        return jsonify({"error": "SKU already exists"}), 409
    product = Product(**payload)
    db.session.add(product)
    db.session.commit()
    invalidate_products_cache(product.id)
    return jsonify(product.to_dict()), 201


@products_bp.put("/<int:product_id>")
@admin_required
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json() or {}
    if "sku" in data and data["sku"] != product.sku:
        if Product.query.filter_by(sku=data["sku"]).first():
            return jsonify({"error": "SKU already exists"}), 409
        product.sku = data["sku"]
    for field in ("name", "description"):
        if field in data:
            setattr(product, field, data[field])
    if "price" in data:
        try:
            product.price = Decimal(str(data["price"]))
        except (InvalidOperation, TypeError):
            return jsonify({"error": "Invalid price"}), 400
    if "stock" in data:
        try:
            product.stock = int(data["stock"])
        except (ValueError, TypeError):
            return jsonify({"error": "Invalid stock"}), 400
    if product.price < 0 or product.stock < 0:
        return jsonify({"error": "Price and stock cannot be negative"}), 400
    if "is_active" in data:
        product.is_active = bool(data["is_active"])
    db.session.commit()
    invalidate_products_cache(product.id)
    return jsonify(product.to_dict())


@products_bp.delete("/<int:product_id>")
@admin_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    product.is_active = False
    db.session.commit()
    invalidate_products_cache(product.id)
    return jsonify({"message": "Product deactivated"})
