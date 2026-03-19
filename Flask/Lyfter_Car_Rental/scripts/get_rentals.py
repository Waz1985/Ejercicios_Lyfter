from flask import request, jsonify
from db.get_rentals_db import get_rentals_db


def get_rentals(rentals):
    filters = request.args.to_dict()

    try:
        rentals = get_rentals_db(filters)
        return jsonify(rentals), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500