
from flask import Flask, jsonify
from scripts.get_users import get_users
from scripts.get_cars import get_cars
from scripts.get_rentals import get_rentals
from scripts.add_user import add_user
from scripts.add_car import add_car
from scripts.create_rental import create_rental
from scripts.change_car_status import change_car_status
from scripts.change_user_status import change_user_status
from scripts.complete_rental import complete_rental
from scripts.change_rental_status import change_rental_status
from scripts.flag_user import flag_user


app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>Hello, World!</h1>"

@app.route("/users", methods=["GET"])
def users():
    users_data = get_users()
    return jsonify(users_data)

@app.route("/users", methods=["POST"])
def add_users():
    return add_user()

@app.route("/users/<int:user_id>", methods=["PATCH"])
def change_users_status(user_id):
    return change_user_status(user_id)

@app.route("/users/<int:user_id>/flag", methods=["PATCH"])
def flag_users(user_id):
    return flag_user(user_id)

@app.route("/cars", methods=["GET"])
def cars():
    cars_data = get_cars()
    return jsonify(cars_data)

@app.route("/cars", methods=["POST"])
def add_cars():
    return add_car()

@app.route("/cars/<int:car_id>", methods=["PATCH"])
def change_cars_status(car_id):
    return change_car_status(car_id)

@app.route("/rentals", methods=["GET"])
def rentals():
    rentals_data = get_rentals()
    return jsonify(rentals_data)

@app.route("/rentals", methods=["POST"])
def create_rentals():
    return create_rental()

@app.route("/rentals/<int:car_id>/complete", methods=["PATCH"])
def complete_rentals(car_id):
    return complete_rental(car_id)

@app.route("/rentals/<int:rental_id>", methods=["PATCH"])
def change_rentals_status(rental_id):
    return change_rental_status(rental_id)

if __name__ == "__main__":
    app.run(host="localhost", debug=True)