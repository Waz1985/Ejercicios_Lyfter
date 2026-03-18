from db_connection import connect_db

def get_users_db(filters):
    connection = connect_db()
    cursor = connection.cursor()
    try:
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

        for key, value in filters.items():
            if key in allowed_filters:
                conditions.append(f"{key} = %s")
                values.append(value)

        if conditions:
            base_query += " WHERE " + " AND ".join(conditions)
        
        cursor.execute(base_query, values)
        rows = cursor.fetchall()

        return [
            {
                "user_id": row[0], 
                "name": row[1], 
                "email": row[2], 
                "username": row[3], 
                "birthday": row[5], 
                "status": row[6]
            }
            for row in rows
        ]

    finally:
        cursor.close()
        connection.close()