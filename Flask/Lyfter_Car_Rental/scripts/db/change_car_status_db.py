from db_connection import connect_db


def change_car_status_db(car_id, new_status):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        query = """
        UPDATE lyfter_car_rental.cars
        SET status = %s
        WHERE car_id = %s
        RETURNING car_id, brand, model, year, status;
        """

        cursor.execute(query, (new_status, car_id))
        updated_car = cursor.fetchone()

        if not updated_car:
            connection.rollback()
            return None

        connection.commit()

        return {
            "car_id": updated_car[0],
            "brand": updated_car[1],
            "model": updated_car[2],
            "year": updated_car[3],
            "status": updated_car[4]
        }

    except Exception as e:
        connection.rollback()
        raise e

    finally:
        cursor.close()
        connection.close()