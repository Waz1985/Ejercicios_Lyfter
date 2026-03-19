from db_connection import connect_db

def change_rental_status_db(rental_id, new_status):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        query = """
        UPDATE lyfter_car_rental.rentals
        SET status = %s
        WHERE rental_id = %s
        RETURNING car_id, rental_date, rental_id, status, user_id;
        """

        cursor.execute(query, (new_status, rental_id))
        updated_rental = cursor.fetchone()

        if not updated_rental:
            connection.rollback()
            return None

        connection.commit()

        return {
                "car_id": updated_rental[0],
                "rental_date": updated_rental[1],
                "rental_id": updated_rental[2],
                "status": updated_rental[3],
                "user_id": updated_rental[4]
            }

    except Exception as e:
        connection.rollback()
        raise e

    finally:
        cursor.close()
        connection.close()