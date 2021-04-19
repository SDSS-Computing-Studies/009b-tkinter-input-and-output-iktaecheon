"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""

import tkinter as tk 
from tkinter import *

win = tk.Tk()
win.title("Madlib")
win.geometry("800x600")

def are():
    a = "are"
    e2.insert(0,a)

def arenot():
    a = "aren't"
    e2.insert(0,a)

def PS4():
    a = "PS4"
    e1.insert(0,a)

def XBOX():
    a = "XBOX"
    e1.insert(0,a)

def Pokemon():
    a = "Pokemon"
    e3.insert(0,a)

def Mario():
    a = "Mario"
    e3.insert(0,a)


Labeldata = StringVar()

label1 = Label(win, width=5, text="My ")
e1 = Entry(win, textvariable=Labeldata, width=10)

Button0 = Button(win, text="PS4", command=PS4)
Button1 = Button(win, text="XBOX", command=XBOX)
Button2 = Button(win, text="are", command=are)
Button3 = Button(win, text="aren't", command=arenot)
Button4 = Button(win, text="Pokemon", command=Pokemon)
Button5 = Button(win, text="Mario", command=Mario)

e2 = Entry(win, text="are/aren't", width=10)
label2 = Label(win, width=15, text="perfect to play")
e3 = Entry(win, text="adj", width=10)
label3 = Label(win, width=15, text="!")

blank1 = Label(win, width=15, text="")


Button0.place(x=110, y=22)
Button1.place(x=165, y=22)
Button2.place(x=110, y=57)
Button3.place(x=140, y=57)
Button4.place(x=250, y=57)
Button5.place(x=320, y=57)

blank1.grid(row=2, column=1)

label1.grid(row=1, column=1)
label2.grid(row=3, column=3)
label3.grid(row=3, column=5)

e1.grid(row=1, column=2)
e2.grid(row=3, column=2)
e3.grid(row=3,column=4)

Labeldata.set = "Noun"

win.mainloop()