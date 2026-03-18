from db_connection import connect_db


def create_rental_db(user_id, car_id, status):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        query = """
        WITH valid_user AS (
            SELECT user_id
            FROM lyfter_car_rental.users
            WHERE user_id = %s AND status = 'ACTIVE'
        ),
        valid_car AS (
            SELECT car_id
            FROM lyfter_car_rental.cars
            WHERE car_id = %s AND status = 'AVAILABLE'
        ),
        new_rental AS (
            INSERT INTO lyfter_car_rental.rentals (user_id, car_id, status)
            SELECT vu.user_id, vc.car_id, 'ACTIVE'
            FROM valid_user vu
            JOIN valid_car vc ON true
            RETURNING rental_id, user_id, car_id, status
        )
        UPDATE lyfter_car_rental.cars c
        SET status = 'RENTED'
        FROM new_rental nr
        WHERE c.car_id = nr.car_id
        RETURNING nr.rental_id, nr.user_id, nr.car_id, nr.status;
        """

        cursor.execute(query, (user_id, car_id, status))
        new_rental = cursor.fetchone()
        connection.commit()

        return {
            "rental_id": new_rental[0],
            "user_id": new_rental[1],
            "car_id": new_rental[2],
            "status": new_rental[3]
            }

    except Exception as e:
        connection.rollback()
        return e

    finally:
        cursor.close()
        connection.close()