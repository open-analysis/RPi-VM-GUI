from tkinter import *
from tkinter.ttk import *

window = Tk()

def buildWidgets(names, images, cmds):
    SIZE = 75
    MAX_ROW = 2
    MAX_COL = 3
    frm = Frame(relief=RAISED)
    for row in range(MAX_ROW):
        frm.rowconfigure(row, weight=1, minsize=SIZE)
        for col in range(MAX_COL):
            frm.columnconfigure(col, weight=1, minsize=SIZE)
            btn_temp = Button(master=frm, text=names[col+row*MAX_COL], image=images[col+row*MAX_COL], command=cmds[col+row*MAX_COL])
            btn_temp.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")

    return frm

def test():
    print("Hello")

# General frame splitting & assigning to larger frames
frm_main = Frame(master=window)

frm_main.pack(fill=BOTH, expand=True)

n = ["a", "b", "c", "d", "e", "f"]
im = ["", "", "", "","", ""]
c = [test, test, test, test, test, test]

frm_test = buildWidgets(n, im, c)
frm_test.master = frm_main

frm_test.pack()

window.mainloop()
