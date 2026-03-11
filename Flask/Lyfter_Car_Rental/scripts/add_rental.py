from db_connection import connect_db

connection = connect_db()
cursor = connection.cursor()

cursor.execute("""
INSERT INTO lyfter_car_rental.rentals
(user_id, car_id, rental_date, return_date, status)
VALUES
(3, 4, '2024-03-04 13:30:00', '2024-03-07 13:30:00', 'ACTIVE');
""")
connection.commit()

