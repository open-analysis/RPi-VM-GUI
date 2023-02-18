from tkinter import *
from tkinter.ttk import *

import build
import func

window = Tk()

# General frame splitting & assigning to larger frames
frm_main = Frame(master=window)

frm_main.pack(fill=BOTH, expand=True)

# Test build
n = ["a", "b", "c", "d", "e", "f"]
im = ["", "", "", "","", ""]
c = [func.test, func.test, func.test, func.test, func.test, func.test]

frm_test = build.buildWidgets(n, im, c)
frm_test.master = frm_main
frm_test.pack()

window.mainloop()
