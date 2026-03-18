from flask import jsonify
from db.complete_rental_db import complete_rental_db


def complete_rental(car_id):
    try:
        updated_car = complete_rental_db(car_id)

        if not updated_car:
            return jsonify({
                "error": "No active rental found for this car or car is not rented."
            }), 400

        return jsonify({
            "message": "Rental completed successfully",
            "data": updated_car
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
