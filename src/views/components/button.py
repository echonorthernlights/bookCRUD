from tkinter import *


def create_button(frame, cmd,  text="default button text", position={"row": 0, "column": 0}):
    button = Button(frame, text=text, width=12, command=lambda: cmd())
    # button = Button(frame, text=text, width=12, command=lambda: cmd() if cmd else None)
    button.grid(row=position["row"], column=position["column"])
    return button

