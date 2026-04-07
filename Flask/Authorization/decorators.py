from functools import wraps
from flask import request, jsonify, g
from db import SessionLocal
from jwt_manager import JWTManager
from models.user import User

jwt_manager = JWTManager()


def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"error": "Authorization header is required"}), 401

        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Invalid authorization format"}), 401

        token = auth_header.replace("Bearer ", "", 1)
        decoded = jwt_manager.decode(token)

        if not decoded:
            return jsonify({"error": "Invalid or expired token"}), 401

        user_id = decoded.get("id")

        if not user_id:
            return jsonify({"error": "Invalid token payload"}), 401

        session = SessionLocal()
        try:
            user = session.get(User, user_id)

            if not user:
                return jsonify({"error": "User not found"}), 401

            g.current_user = user
            return f(*args, **kwargs)
        finally:
            session.close()

    return decorated


def require_role(*allowed_roles):
    def wrapper(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            current_user = getattr(g, "current_user", None)

            if not current_user:
                return jsonify({"error": "Unauthorized"}), 401

            if current_user.role not in allowed_roles:
                return jsonify({"error": "Forbidden"}), 403

            return f(*args, **kwargs)

        return decorated

    return wrapper