from tkinter import *
from tkinter import ttk


def create_label(frame, text="default label text", row=0, column=0):

    return ttk.Label(frame, text=text).grid(row=row, column=column)
