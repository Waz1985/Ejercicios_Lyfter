from db_connection import connect_db

connection = connect_db()
cursor = connection.cursor()

cursor.execute("""
INSERT INTO lyfter_car_rental.users
(name, email, username, password, birthday, status)
VALUES
('Maria Sotella','mariasotela@test.com','mariasotela1','123','1985-04-12','ACTIVE');
""")
connection.commit()