from flask import request, jsonify
from db_connection import connect_db


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

    
    connection = connect_db()
    cursor = connection.cursor()

    try:
        query = ("""
        INSERT INTO lyfter_car_rental.cars
        (brand, model, year, status)
        VALUES (%s, %s, %s, %s)
        RETURNING car_id, brand, model, year, status;
        """)

        cursor.execute(query, (
            data["brand"],
            data["model"],
            data["year"],
            data["status"]
        ))

        new_car = cursor.fetchone()
        connection.commit()
        
        return jsonify({
        "message": "Car created successfully",
        "data": {
            "car_id": new_car[0],
            "brand": new_car[1],
            "model": new_car[2],
            "year": new_car[3],
            "status": new_car[4]
            }
        }), 201
    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)}), 500
    
    finally:
        cursor.close()
        connection.close()
