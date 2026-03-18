from db_connection import connect_db


def add_user_db(name, email, username, password, birthday, status):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        query = ("""
        INSERT INTO lyfter_car_rental.users
        (name, email, username, password, birthday, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING user_id, name, email, username, birthday, status;
        """)

        cursor.execute(query, (name, email, username, password, birthday, status))
        new_user = cursor.fetchone()
        connection.commit()
        
        return {
            "user_id": new_user[0],
            "name": new_user[1],
            "email": new_user[2],
            "username": new_user[3],
            "birthday": new_user[4],
            "status": new_user[5]
        }
    
    except Exception as e:
        connection.rollback()
        return e
    
    finally:
        cursor.close()
        connection.close()