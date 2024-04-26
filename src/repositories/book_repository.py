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


def get_book(book_id):

    try:
        connection = connect_to_db()
        query = "SELECT * FROM books WHERE isbn=%s"
        cursor = connection.cursor()

        cursor.execute(query, (book_id,))
        book = cursor.fetchone()
        connection.commit()

        print("Book returned successfully !")
        connection.close()
        return book
    except Exception as error:
        print("Error : ", error)


def update_book(book, book_id):

    try:
        connection = connect_to_db()
        query = "UPDATE books SET title=%s, author=%s, year=%s, isbn=%s  WHERE id=%s"
        cursor = connection.cursor()

        cursor.execute(query, (book.title, book.author, book.year, book.isbn, book_id,))
        connection.commit()

        print("Book updated successfully !")
        connection.close()
        return 0
    except Exception as error:
        print("Error : ", error)


def delete_book(book_id):

    try:
        connection = connect_to_db()
        query = "DELETE FROM books WHERE id=%s"
        cursor = connection.cursor()

        cursor.execute(query, (book_id,))
        connection.commit()

        print("Book deleted successfully !")
        connection.close()
        return 0
    except Exception as error:
        print("Error : ", error)
