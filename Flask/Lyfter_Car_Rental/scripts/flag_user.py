from flask import jsonify
from db.flag_user_db import flag_user_db

def flag_user(user_id):
    try:
        flagged_user = flag_user_db(user_id)

        if not flagged_user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({
            "message": "User flagged successfully",
            "data": flagged_user
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500