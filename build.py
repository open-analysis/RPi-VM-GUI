from tkinter import *
from tkinter.ttk import *

import operations as ops

def buildWidgets(names, images, cmds, start=0):
    SIZE = 75
    MAX_ROW = 2
    MAX_COL = 3
    MAX_WIDGETS = 6
    currPage = []
    
    frm = Frame(relief=RAISED)
    # Building the buttons

    namesLen = len(names)

    for i in range(MAX_WIDGETS):
        # If there's less widgets than the max, break
        if i == (namesLen-start):
            break

        # Check if the current section of the list will overflow
        if (namesLen-start) > MAX_WIDGETS and i == (MAX_WIDGETS-1):
            # make the last button (this current one) be a link to the next page
            currPage.append(["More", "", lambda: ops.openScreenExt(names, images, cmds, (start+MAX_WIDGETS-1))])
            break
        currPage.append([names[start+i], images[start+i], cmds[start+i]])

    # Add blank buttons if there's less than 6
    if len(currPage) < 6:
        for _ in range(6-len(currPage)):
            currPage.append(["", "", None])

    # Implementing the buttons
    for row in range(MAX_ROW):
        frm.rowconfigure(row, weight=1, minsize=SIZE)
        for col in range(MAX_COL):
            frm.columnconfigure(col, weight=1, minsize=SIZE)

            btn_temp = Button(master=frm, text=currPage[col+row*MAX_COL][0], 
                        image=currPage[col+row*MAX_COL][1], 
                        command=currPage[col+row*MAX_COL][2])
                        
            btn_temp.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")

    return frm


def destroyWidgets(frm):
    frm.destroy()


def moveFolder(old_frm, names, images, cmds):
    destroyWidgets(old_frm)

    return buildWidgets(names, images, cmds)