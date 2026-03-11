from flask import request
from db_connection import connect_db

def get_users():
    connection = connect_db()
    cursor = connection.cursor()

    base_query = "SELECT * FROM lyfter_car_rental.users"
    conditions = []
    values = []
    allowed_filters = [
        "user_id",
        "name",
        "email",
        "username",
        "birthday",
        "status"
    ]

    for key, value in request.args.items():
        if key in allowed_filters:
            conditions.append(f"{key} = %s")
            values.append(value)
    if conditions:
        base_query += " WHERE " + " AND ".join(conditions)
    
    print(conditions)
    print(values)
    print(base_query)
    cursor.execute(base_query, values)

    rows = cursor.fetchall()
    users = []

    for row in rows:
        users.append({
        "User ID": row[0], 
        "Name": row[1], 
        "Email": row[2], 
        "Username": row[3], 
        "Birthday": row[5], 
        "Status": row[6] 
        })

    return users