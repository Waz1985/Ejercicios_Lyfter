from db_connection import connect_db

def flag_user_db(user_id):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        query = """
        UPDATE lyfter_car_rental.users
        SET status = 'DELINQUENT'
        WHERE user_id = %s
        RETURNING user_id, name, email, username, birthday, status;
        """

        cursor.execute(query, (user_id,))
        updated_user = cursor.fetchone()

        if not updated_user:
            connection.rollback()
            return None

        connection.commit()

        return {
                "user_id": updated_user[0],
                "name": updated_user[1],
                "email": updated_user[2],
                "username": updated_user[3],
                "birthday": updated_user[4],
                "status": updated_user[5]
            }

    except Exception as e:
        connection.rollback()
        raise e

    finally:
        cursor.close()
        connection.close()