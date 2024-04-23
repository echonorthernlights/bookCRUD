import psycopg2
from psycopg2 import Error


def connect_to_db():
    connection = None

    try:
        connection = psycopg2.connect(
            user="postgres",
            password="root1234",
            host="localhost",
            port="5432",
            database="Library_DB"
        )
        print("You are connected...")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)
    # finally:
    #     # Closing the database connection.
    #     if connection:
    #         connection.close()
    #         print("PostgreSQL connection is closed")
    return connection
