from db_connection import connect_db


def get_available_cars_db():
    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute("""
        SELECT car_id, brand, model, year, status
        FROM lyfter_car_rental.cars
        WHERE status = 'AVAILABLE';
        """)

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