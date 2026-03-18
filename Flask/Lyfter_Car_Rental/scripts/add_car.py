from flask import request, jsonify
from db.add_car_db import add_car_db


def add_car():
    data = request.get_json()

    required_fields = ["brand", "model", "year", "status"]
    allowed_status = ["AVAILABLE", "UNAVAILABLE", "RENTED"]

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            return jsonify({"error": f"Field '{field}' is required"}), 400

    if data["status"] not in allowed_status:
        return jsonify({"error": "Invalid status"}), 400

    try:
        new_car = add_car_db (
            data["brand"],
            data["model"],
            data["year"],
            data["status"]
        )

        return jsonify({
            "message": "Car created successfully",
            "data": new_car
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500