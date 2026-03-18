from flask import request, jsonify
from db.get_cars_db import get_cars_db


def get_cars():
    filters = request.args.to_dict()

    try:
        cars = get_cars_db(filters)
        return jsonify(cars), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500