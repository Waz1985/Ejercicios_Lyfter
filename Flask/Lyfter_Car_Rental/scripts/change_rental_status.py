from flask import request, jsonify
from db.change_rental_status_db import change_rental_status_db

def change_rental_status(rental_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    new_status = data.get("status")

    allowed_status = ["ACTIVE", "COMPLETED"]

    if new_status not in allowed_status:
        return jsonify({"error": "Invalid status"}), 400

    try:
        updated_rental = change_rental_status_db(rental_id, new_status)

        if not updated_rental:
            return jsonify({"error": "Rental not found"}), 404

        return jsonify({
            "message": "Rental status updated successfully",
            "data": updated_rental
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
