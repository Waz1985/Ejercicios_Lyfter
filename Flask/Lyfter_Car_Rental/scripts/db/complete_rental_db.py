from db_connection import connect_db


def complete_rental_db(car_id):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        query = """
        WITH valid_car AS (
            SELECT car_id
            FROM lyfter_car_rental.cars
            WHERE car_id = %s AND status = 'RENTED'
        ),
        complete_rental AS (
            UPDATE lyfter_car_rental.rentals r
            SET status = 'COMPLETED',
                return_date = NOW()
            FROM valid_car vc
            WHERE r.car_id = vc.car_id
            AND r.status = 'ACTIVE'
            RETURNING r.car_id
        )
        UPDATE lyfter_car_rental.cars c
        SET status = 'AVAILABLE'
        FROM complete_rental cr
        WHERE c.car_id = cr.car_id
        RETURNING c.car_id, c.status;
        """

        cursor.execute(query, (car_id,))
        updated_car = cursor.fetchone()

        if not updated_car:
            connection.rollback()
            return None

        connection.commit()

        return {
                "car_id": updated_car[0],
                "status": updated_car[1]
            }

    except Exception as e:
        connection.rollback()
        raise e

    finally:
        cursor.close()
        connection.close()