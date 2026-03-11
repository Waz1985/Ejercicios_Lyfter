from flask import request, jsonify
from db_connection import connect_db

def flag_user(user_id):

    connection = connect_db()
    cursor = connection.cursor()

    try:
        query = """
        UPDATE lyfter_car_rental.users
        SET status = 'DELINQUENT'
        WHERE user_id = %s
        RETURNING user_id, name, email, username, birthday, status;
        """

        cursor.execute(query, (user_id,))

        updated_user = cursor.fetchone()

        if not updated_user:
            connection.rollback()
            return jsonify({"error": "User not found"}), 404

        connection.commit()

        return jsonify({
            "message": "User flagged successfully",
            "data": {
                "user_id": updated_user[0],
                "name": updated_user[1],
                "email": updated_user[2],
                "username": updated_user[3],
                "birthday": updated_user[4],
                "status": updated_user[5]
            }
        })

    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        connection.close()