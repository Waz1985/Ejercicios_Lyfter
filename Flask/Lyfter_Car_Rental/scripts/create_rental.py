from flask import request, jsonify
from db.create_rental_db import create_rental_db


from flask import request, jsonify
from db.create_rental_db import create_rental_db


def create_rental():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    user_id = data.get("user_id")
    car_id = data.get("car_id")
    status = data.get("status", "ACTIVE")

    if not user_id:
        return jsonify({"error": "Field 'user_id' is required"}), 400

    if not car_id:
        return jsonify({"error": "Field 'car_id' is required"}), 400

    try:
        new_rental = create_rental_db(user_id, car_id, status)

        if not new_rental:
            return jsonify({"error": "User inactive, car unavailable, or rental could not be created"}), 400

        return jsonify({
            "message": "Rental created successfully",
            "data": new_rental
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
