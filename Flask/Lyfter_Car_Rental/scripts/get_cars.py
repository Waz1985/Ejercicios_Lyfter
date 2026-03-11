from flask import request
from db_connection import connect_db

def get_cars():
    connection = connect_db()
    cursor = connection.cursor()

    base_query = "SELECT * FROM lyfter_car_rental.cars"
    conditions = []
    values = []
    allowed_filters = [
        "car_id",
        "brand",
        "model",
        "year",
        "status"
    ]

    for key, value in request.args.items():
        if key in allowed_filters:
            conditions.append(f"{key} = %s")
            values.append(value)
    if conditions:
        base_query += " WHERE " + " AND ".join(conditions)
        
    cursor.execute(base_query, values)

    rows = cursor.fetchall()
    cars = []

    for row in rows:
        cars.append({
        "Car ID": row[0], 
        "Brand": row[1], 
        "Model": row[2], 
        "Year": row[3], 
        "Status": row[4] 
        })

    return cars