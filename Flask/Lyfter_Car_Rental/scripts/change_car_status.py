from flask import request, jsonify
from db_connection import connect_db

def change_car_status(car_id):

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    new_status = data.get("status")

    allowed_status = ["AVAILABLE", "RENTED", "UNAVAILABLE", "MAINTENANCE"]

    if new_status not in allowed_status:
        return jsonify({"error": "Invalid status"}), 400

    connection = connect_db()
    cursor = connection.cursor()

    try:

        query = """
        UPDATE lyfter_car_rental.cars
        SET status = %s
        WHERE car_id = %s
        RETURNING car_id, brand, model, year, status;
        """

        cursor.execute(query, (new_status, car_id))

        updated_car = cursor.fetchone()

        if not updated_car:
            connection.rollback()
            return jsonify({"error": "Car not found"}), 404

        connection.commit()

        return jsonify({
            "message": "Car status updated successfully",
            "data": {
                "car_id": updated_car[0],
                "brand": updated_car[1],
                "model": updated_car[2],
                "year": updated_car[3],
                "status": updated_car[4]
            }
        })

    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        connection.close()