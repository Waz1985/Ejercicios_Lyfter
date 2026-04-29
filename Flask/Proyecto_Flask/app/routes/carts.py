from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from ..auth import current_user
from ..extensions import db
from ..models import Cart, CartItem, Product

carts_bp = Blueprint("carts", __name__)


def _owned_open_cart_or_404(cart_id):
    cart = Cart.query.get_or_404(cart_id)
    if cart.user_id != current_user().id:
        return None, (jsonify({"error": "You cannot access this cart"}), 403)
    if cart.status != "open":
        return None, (jsonify({"error": "The cart is not open"}), 400)
    return cart, None


@carts_bp.post("")
@jwt_required()
def create_cart():
    cart = Cart(user_id=current_user().id)
    db.session.add(cart)
    db.session.commit()
    return jsonify(cart.to_dict()), 201


@carts_bp.get("")
@jwt_required()
def list_carts():
    carts = Cart.query.filter_by(user_id=current_user().id).order_by(Cart.id.desc()).all()
    return jsonify([cart.to_dict() for cart in carts])


@carts_bp.get("/<int:cart_id>")
@jwt_required()
def get_cart(cart_id):
    cart = Cart.query.get_or_404(cart_id)
    if cart.user_id != current_user().id:
        return jsonify({"error": "You cannot access this cart"}), 403
    return jsonify(cart.to_dict())


@carts_bp.post("/<int:cart_id>/items")
@jwt_required()
def add_item(cart_id):
    cart, error = _owned_open_cart_or_404(cart_id)
    if error:
        return error
    data = request.get_json() or {}
    product = Product.query.get_or_404(data.get("product_id"))
    try:
        quantity = int(data.get("quantity", 1))
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid quantity"}), 400
    if quantity <= 0:
        return jsonify({"error": "Quantity must be greater than zero"}), 400
    if not product.is_active:
        return jsonify({"error": "Inactive product"}), 400

    item = CartItem.query.filter_by(cart_id=cart.id, product_id=product.id).first()
    new_quantity = quantity + (item.quantity if item else 0)
    if new_quantity > product.stock:
        return jsonify({"error": "Insufficient stock"}), 400
    if item:
        item.quantity = new_quantity
    else:
        db.session.add(CartItem(cart_id=cart.id, product_id=product.id, quantity=quantity))
    db.session.commit()
    return jsonify(cart.to_dict())


@carts_bp.put("/<int:cart_id>/items/<int:item_id>")
@jwt_required()
def update_item(cart_id, item_id):
    cart, error = _owned_open_cart_or_404(cart_id)
    if error:
        return error
    item = CartItem.query.filter_by(id=item_id, cart_id=cart.id).first_or_404()
    try:
        quantity = int((request.get_json() or {}).get("quantity"))
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid quantity"}), 400
    if quantity <= 0:
        return jsonify({"error": "Quantity must be greater than zero"}), 400
    if quantity > item.product.stock:
        return jsonify({"error": "Insufficient stock"}), 400
    item.quantity = quantity
    db.session.commit()
    return jsonify(cart.to_dict())


@carts_bp.delete("/<int:cart_id>/items/<int:item_id>")
@jwt_required()
def remove_item(cart_id, item_id):
    cart, error = _owned_open_cart_or_404(cart_id)
    if error:
        return error
    item = CartItem.query.filter_by(id=item_id, cart_id=cart.id).first_or_404()
    db.session.delete(item)
    db.session.commit()
    return jsonify(cart.to_dict())
