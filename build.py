from tkinter import *
from tkinter.ttk import *

def buildWidgets(names, images, cmds):
    SIZE = 75
    MAX_ROW = 2
    MAX_COL = 3
    frm = Frame(relief=RAISED)
    for row in range(MAX_ROW):
        frm.rowconfigure(row, weight=1, minsize=SIZE)
        for col in range(MAX_COL):
            frm.columnconfigure(col, weight=1, minsize=SIZE)
            # Check if the list is long enough
            if (col+row*MAX_COL) < len(names):
                currName = names[col+row*MAX_COL]
                currImage = images[col+row*MAX_COL]
                currCmd = cmds[col+row*MAX_COL]
            # Otherwise make the button blank
            else:
                currName = ""
                currImage = ""
                currCmd = None

            btn_temp = Button(master=frm, text=currName, 
                        image=currImage, 
                        command=currCmd)
                        
            btn_temp.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")

    return frm


def destroyWidgets(frm):
    frm.destroy()


def moveFolder(old_frm, names, images, cmds):
    destroyWidgets(old_frm)

    return buildWidgets(names, images, cmds)