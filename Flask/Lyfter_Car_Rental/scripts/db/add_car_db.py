from db_connection import connect_db

def add_car_db(brand, model, year, status):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        query = """
        INSERT INTO lyfter_car_rental.cars
        (brand, model, year, status)
        VALUES (%s, %s, %s, %s)
        RETURNING car_id, brand, model, year, status;
        """

        cursor.execute(query, (brand, model, year, status))
        new_car = cursor.fetchone()
        connection.commit()

        return {
            "car_id": new_car[0],
            "brand": new_car[1],
            "model": new_car[2],
            "year": new_car[3],
            "status": new_car[4]
        }

    except Exception as e:
        connection.rollback()
        raise e

    finally:
        cursor.close()
        connection.close()