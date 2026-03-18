from db_connection import connect_db


def get_cars_db(filters):
    connection = connect_db()
    cursor = connection.cursor()

    try:
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
                "car_id": row[0],
                "brand": row[1],
                "model": row[2],
                "year": row[3],
                "status": row[4]
            }
            for row in rows
        ]

    finally:
        cursor.close()
        connection.close()