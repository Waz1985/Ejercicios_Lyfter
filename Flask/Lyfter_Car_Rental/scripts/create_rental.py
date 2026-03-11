from flask import request, jsonify
from db_connection import connect_db


def create_rental():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    user_id = data.get("user_id")
    car_id = data.get("car_id")

    if not user_id:
        return jsonify({"error": "Field 'user_id' is required"}), 400

    if not car_id:
        return jsonify({"error": "Field 'car_id' is required"}), 400

    connection = connect_db()
    cursor = connection.cursor()

    try:
        query = """
        WITH valid_user AS (
            SELECT user_id
            FROM lyfter_car_rental.users
            WHERE user_id = %s AND status = 'ACTIVE'
        ),
        valid_car AS (
            SELECT car_id
            FROM lyfter_car_rental.cars
            WHERE car_id = %s AND status = 'AVAILABLE'
        ),
        new_rental AS (
            INSERT INTO lyfter_car_rental.rentals (user_id, car_id, status)
            SELECT vu.user_id, vc.car_id, 'ACTIVE'
            FROM valid_user vu
            JOIN valid_car vc ON true
            RETURNING rental_id, user_id, car_id, status
        )
        UPDATE lyfter_car_rental.cars c
        SET status = 'RENTED'
        FROM new_rental nr
        WHERE c.car_id = nr.car_id
        RETURNING nr.rental_id, nr.user_id, nr.car_id, nr.status;
        """

        cursor.execute(query, (user_id, car_id))
        rental_created = cursor.fetchone()

        if not rental_created:
            connection.rollback()
            return jsonify({
                "error": "Rental could not be created. Verify that user is ACTIVE and car is AVAILABLE."
            }), 400

        connection.commit()

        return jsonify({
            "message": "Rental created successfully",
            "data": {
                "rental_id": rental_created[0],
                "user_id": rental_created[1],
                "car_id": rental_created[2],
                "status": rental_created[3]
            }
        }), 201

    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        connection.close()