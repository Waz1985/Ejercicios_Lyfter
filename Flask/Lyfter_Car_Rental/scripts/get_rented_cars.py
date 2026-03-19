from db_connection import connect_db

connection = connect_db()
cursor = connection.cursor()

cursor.execute("""
SELECT * FROM lyfter_car_rental.cars
WHERE status = 'RENTED';
""")
connection.commit()