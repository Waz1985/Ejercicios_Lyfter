from flask import jsonify
from db.get_available_cars_db import get_available_cars_db


def get_available_cars():
    cars = get_available_cars_db()
    return jsonify(cars), 200