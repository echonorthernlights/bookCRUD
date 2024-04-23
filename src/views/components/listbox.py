from tkinter import *


def create_listbox(frame,position, dimension, span):
    listbox = Listbox(frame, height=dimension["height"], width=dimension["width"])
    listbox.grid(row=position["row"], column=position["column"], rowspan=span["rowspan"], columnspan=span["columnspan"])
    return listbox
