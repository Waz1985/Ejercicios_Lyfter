from db_connection import connect_db

connection = connect_db()
cursor = connection.cursor()

cursor.execute("""
INSERT INTO lyfter_car_rental.cars
(brand, model, year, status)
VALUES
('Honda','CRV',2007,'AVAILABLE')
""")
connection.commit()