from tkinter import *


def create_entry(frame, row=0, column=0):
    title_text = StringVar()
    entry = Entry(frame, textvariable=title_text)
    entry.grid(row=row, column=column)
    return entry
