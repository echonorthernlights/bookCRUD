from src.config.connect_database import connect_to_db


def add_book(book):
    try:
        connection = connect_to_db()
        query = "INSERT INTO books (title, author, year, isbn) VALUES (%s, %s, %s, %s)"
        values = (book.title, book.author, book.year, book.isbn)

        cursor = connection.cursor()

        cursor.execute(query, values)
        connection.commit()

        print("Book added successfully to database !")
        connection.close()
    except Exception as error:
        print("Error : ", error)


def get_books():
    try:
        connection = connect_to_db()
        query = "SELECT * FROM books"

        cursor = connection.cursor()

        cursor.execute(query)
        books = cursor.fetchall()
        connection.commit()

        print("Books list returned successfully !")
        connection.close()
        return books
    except Exception as error:
        print("Error : ", error)

