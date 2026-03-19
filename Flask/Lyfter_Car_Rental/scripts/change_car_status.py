from flask import request, jsonify
from db.change_car_status_db import change_car_status_db


def change_car_status(car_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    new_status = data.get("status")

    allowed_status = ["AVAILABLE", "RENTED", "UNAVAILABLE", "MAINTENANCE"]

    if new_status not in allowed_status:
        return jsonify({"error": "Invalid status"}), 400

    try:
        updated_car = change_car_status_db(car_id, new_status)

        if not updated_car:
            return jsonify({"error": "Car not found"}), 404

        return jsonify({
            "message": "Car status updated successfully",
            "data": updated_car
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500