from tkinter import *
from tkinter.ttk import *

import vars
import func
import operations as ops

window = Tk()

# General frame splitting & assigning to larger frames
frm_win = Frame(master=window)
frm_win.pack(fill=BOTH, expand=True)


frm_main = Frame()
vars.setFrmMain(frm_main)
btn_return = Button(master=frm_win, text="Return", command=lambda: ops.openScreen(vars.top)) 
btn_return.pack()

ops.openScreen(vars.top)

window.mainloop()
