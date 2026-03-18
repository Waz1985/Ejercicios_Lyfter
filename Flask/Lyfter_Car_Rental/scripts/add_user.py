from flask import request, jsonify
from db.add_user_db import add_user_db


def add_user():
    data = request.get_json()

    required_fields = ["name", "email", "username", "password", "birthday", "status"]
    allowed_status = ["ACTIVE", "INACTIVE", "SUSPENDED", "DELINQUENT"]

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            return jsonify({"error": f"Field '{field}' is required"}), 400

    if data["status"] not in allowed_status:
        return jsonify({"error": "Invalid status"}), 400

    try:
        new_user = add_user_db (
            data["name"],
            data["email"],
            data["username"],
            data["password"],
            data["birthday"],
            data["status"]
        )

        return jsonify({
        "message": "User created successfully",
        "data": new_user
        }), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500