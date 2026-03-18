from db_connection import connect_db

def get_rentals_db(filters):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        base_query = "SELECT * FROM lyfter_car_rental.rentals"
        conditions = []
        values = []

        allowed_filters = [
            "rental_id",
            "user_id",
            "car_id",
            "rental_date",
            "return_date",
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
                "Rental ID": row[0], 
                "User ID": row[1], 
                "Car ID": row[2], 
                "Rental Date": row[3], 
                "Return Date": row[4],
                "Status": row[5]
            }
            for row in rows
        ]

    finally:
        cursor.close()
        connection.close()
