from tkinter import END

from src.models.book import Book
from src.repositories.book_repository import add_book, get_books


def add_new_book(title, author, year, isbn):
    print("Start passing data to Book model")
    book = Book(title=title.get(), author=author.get(), year=year.get(), isbn=isbn.get())
    print("End passing data to Book model")
    print("Start passing data to book repository")
    add_book(book)
    print("End passing data to book repository")
    title.delete(0, END)
    author.delete(0, END)
    year.delete(0, END)
    isbn.delete(0, END)


def get_all_books(data_list):
    print("Start getting books list from database")

    print("End passing data to Book model")
    books = get_books()
    if books is None:
        print("No books found")
        return
    data_list.delete(0, END)
    data_list.insert(END, ["ID", "Title","Author", "Year", "ISBN"])
    for book in books:

        data_list.insert(END, book)

    print("Start passing data to book repository")

    print("End passing data to book repository")