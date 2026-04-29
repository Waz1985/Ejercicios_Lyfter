from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from ..auth import admin_required, current_user
from ..extensions import db
from ..models import User

users_bp = Blueprint("users", __name__)


@users_bp.get("/me")
@jwt_required()
def me():
    return jsonify(current_user().to_dict())


@users_bp.get("")
@admin_required
def list_users():
    return jsonify([user.to_dict() for user in User.query.order_by(User.id).all()])


@users_bp.get("/<int:user_id>")
@admin_required
def get_user(user_id):
    return jsonify(User.query.get_or_404(user_id).to_dict())


@users_bp.post("")
@admin_required
def create_user():
    data = request.get_json() or {}
    required = ["name", "email", "password", "role"]
    missing = [field for field in required if not data.get(field)]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400
    if data["role"] not in ("admin", "client"):
        return jsonify({"error": "Invalid role"}), 400
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email is already registered"}), 409

    user = User(name=data["name"], email=data["email"], role=data["role"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


@users_bp.put("/<int:user_id>")
@admin_required
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json() or {}
    if "email" in data and data["email"] != user.email:
        if User.query.filter_by(email=data["email"]).first():
            return jsonify({"error": "Email is already registered"}), 409
        user.email = data["email"]
    if "name" in data:
        user.name = data["name"]
    if "role" in data:
        if data["role"] not in ("admin", "client"):
            return jsonify({"error": "Invalid role"}), 400
        user.role = data["role"]
    if "is_active" in data:
        user.is_active = bool(data["is_active"])
    if data.get("password"):
        user.set_password(data["password"])
    db.session.commit()
    return jsonify(user.to_dict())


@users_bp.delete("/<int:user_id>")
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    user.is_active = False
    db.session.commit()
    return jsonify({"message": "User deactivated"})
