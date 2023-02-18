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
c = [func.printInput, func.test2, func.test3, func.test4, func.test5, func.test6]
p = ["Input", "Test2", "test3", "test4", "test5", "test6"]

frm_test = build.buildWidgets(n, im, c, p)
frm_test.master = frm_main
frm_test.pack()

window.mainloop()
