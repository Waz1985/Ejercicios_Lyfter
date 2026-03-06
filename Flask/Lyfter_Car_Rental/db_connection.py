import psycopg2

def connect_db ():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        user="postgres",
        password="admin",
        dbname="lyfter_db",
    )
    print("Connected to database!")

    return connection

