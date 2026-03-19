from flask import request, jsonify
from db.get_users_db import get_users_db

def get_users():
    filters = request.args.to_dict()

    try:
        users = get_users_db(filters)
        return jsonify(users), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500