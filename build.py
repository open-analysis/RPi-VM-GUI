from tkinter import *
from tkinter.ttk import *

def buildWidgets(names, images, cmds, cmd_params):
    SIZE = 75
    MAX_ROW = 2
    MAX_COL = 3
    frm = Frame(relief=RAISED)
    for row in range(MAX_ROW):
        frm.rowconfigure(row, weight=1, minsize=SIZE)
        for col in range(MAX_COL):
            frm.columnconfigure(col, weight=1, minsize=SIZE)
            print(f"{col+row*MAX_COL}")
            btn_temp = Button(master=frm, text=names[col+row*MAX_COL], 
                        image=images[col+row*MAX_COL], 
                        command=lambda: cmds[col+row*MAX_COL](cmd_params[col+row*MAX_COL]))
                        
            btn_temp.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")

    return frm