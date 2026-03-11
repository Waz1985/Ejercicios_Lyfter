from flask import request, jsonify
from db_connection import connect_db


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

    
    connection = connect_db()
    cursor = connection.cursor()

    try:
        query = ("""
        INSERT INTO lyfter_car_rental.users
        (name, email, username, password, birthday, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING user_id, name, email, username, birthday, status;
        """)

        cursor.execute(query, (
            data["name"],
            data["email"],
            data["username"],
            data["password"],
            data["birthday"],
            data["status"]
        ))

        new_user = cursor.fetchone()
        connection.commit()
        
        return jsonify({
        "message": "User created successfully",
        "data": {
            "user_id": new_user[0],
            "name": new_user[1],
            "email": new_user[2],
            "username": new_user[3],
            "birthday": new_user[4],
            "status": new_user[5]
            }
        }), 201
    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)}), 500
    
    finally:
        cursor.close()
        connection.close()