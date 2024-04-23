from tkinter import ttk
from tkinter import *
from src.views.components.label import create_label
from src.views.components.entry import create_entry
from src.views.components.listbox import create_listbox
from src.views.components.scrollbar import create_scrollbar
from src.views.components.button import create_button
from src.controllers.book_controller import add_new_book, get_all_books, get_single_book


def create_frame(rt):
    frm = ttk.Frame(rt, padding=10)
    frm.grid()
    return frm


root = Tk()
frame = create_frame(root)

create_label(frame, text="Title : ", row=0, column=0)
create_label(frame, text="Author : ", row=0, column=2)
create_label(frame, text="Year : ", row=1, column=0)
create_label(frame, text="ISBN : ", row=1, column=2)

title_entry = create_entry(frame, row=0, column=1)
author_entry = create_entry(frame, row=0, column=3)
year_entry = create_entry(frame, row=1, column=1)
isbn_entry = create_entry(frame, row=1, column=3)

data_list = create_listbox(frame, {"row": 2, "column": 0},
                           {"height": 6, "width": 65},
                           {"rowspan": 6, "columnspan": 2})

create_scrollbar(frame, data_list, row=2, column=2)

create_button(frame, cmd=lambda: get_all_books(data_list), text="Select All", position={"row": 2, "column": 3})
create_button(frame, cmd=lambda: get_single_book(data_list, book_isbn=isbn_entry), text="Select One", position={"row": 3, "column": 3})
create_button(frame, cmd=lambda: add_new_book(title_entry,
                                              author_entry,
                                              year_entry,
                                              isbn_entry),
              text="Add One", position={"row": 4, "column": 3}, )

# create_button(frame, cmd=None, text="Update One", position={"row": 5, "column": 3})
# create_button(frame, cmd=None, text="Delete One", position={"row": 6, "column": 3})
# create_button(frame, cmd=None, text="Delete Selected", position={"row": 7, "column": 3})
# create_button(frame, text="Quit", cmd=None, position={"row": 7, "column": 3})

root.mainloop()
