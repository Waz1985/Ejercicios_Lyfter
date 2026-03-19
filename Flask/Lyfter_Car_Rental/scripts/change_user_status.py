from flask import request, jsonify
from db.change_user_status_db import change_user_status_db

def change_user_status(user_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    new_status = data.get("status")

    allowed_status = ["ACTIVE", "INACTIVE", "SUSPENDED", "DELINQUENT"]

    if new_status not in allowed_status:
        return jsonify({"error": "Invalid status"}), 400

    try:
        updated_user = change_user_status_db(user_id, new_status)

        if not updated_user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({
            "message": "User status updated successfully",
            "data": updated_user
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500