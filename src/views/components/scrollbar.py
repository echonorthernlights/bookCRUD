from tkinter import *


def create_scrollbar(frame, listbox, row=0, column=0):
    scrollbar = Scrollbar(frame)
    scrollbar.grid(row=row, column=column, rowspan=6)
    listbox.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=listbox.yview)
    return scrollbar
