"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""

import tkinter as tk 
from tkinter import *



win = tk.Tk()
win.title("Factorization Machine")

win.geometry("800x400")


def factorize():
    finalTry.insert(0,"                    ")
    b = int(Entry1.get())
    c = int(Entry2.get())
    
    nums = []
    for i in range(1, c + 1):
        if c % i == 0:
            nums.append(i)
    nums.sort()
    print(nums)
    count = 0
    xval = ""
    yval = ""
    q = 0
    w = -1
    while (nums[q]+nums[w] != b):
        count = count+1
        w = w-1
        q=q+1
       
        xval = nums[q]
        yval = nums[w]

        xval = str(xval)
        yval = str(yval)

    finalTry.insert(0,("(x+", nums[q], ")(x+", nums[w], ")"))
    print(xval + "  " + yval)




label1 = Label(win, width=2, text="x^2")
label2 = Label(win, width=2, text="x")
label3 = Label(win, text="+", width=3)
label4 = Label(win, text="+", width=3)
Button1 = Button(win, text="factorize", command=factorize)


Entry1 = Entry(win, text="b", width=3)
Entry2 = Entry(win, text="c", width=3)
finalTry = Entry(win, text="adj", width=15)



label1.grid(row=1, column=1)
label2.grid(row=1, column=4)
label3.grid(row=1, column=2)
label4.grid(row=1, column=5)

Button1.place(x=0, y=100)


Entry1.grid(row=1, column=3)
Entry2.grid(row=1, column=6)
finalTry.place(x=150, y=100)

win.mainloop()
