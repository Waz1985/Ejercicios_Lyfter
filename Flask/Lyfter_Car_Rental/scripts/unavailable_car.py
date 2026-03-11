from db_connection import connect_db

connection = connect_db()
cursor = connection.cursor()

cursor.execute("""
UPDATE lyfter_car_rental.cars
SET status = 'UNAVAILABLE' 
WHERE car_id = 7;
""")
connection.commit()

