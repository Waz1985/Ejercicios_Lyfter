from db_connection import connect_db

connection = connect_db()
cursor = connection.cursor()

cursor.execute("""
SELECT * FROM lyfter_car_rental.cars
WHERE status = 'AVAILABLE';
""")

rows = cursor.fetchall()

for row in rows:
    print(f"Car ID: {row[0]}, Brand: {row[1]}, Model: {row[2]}, Status: {row[4]}")
connection.commit()