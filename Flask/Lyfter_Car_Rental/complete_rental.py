from db_connection import connect_db

connection = connect_db()
cursor = connection.cursor()

cursor.execute("""
UPDATE lyfter_car_rental.users 
SET status = 'ACTIVE'
WHERE user_id = 9;
""")
connection.commit()