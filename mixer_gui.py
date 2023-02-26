import tkinter as tk 

import vars
import func
import operations as ops

import test

window = tk.Tk()
window.title("Mixer")
window.geometry("800x600")

# General frame splitting & assigning to larger frames
frm_win = tk.Frame(master=window)
frm_win.pack(fill=tk.BOTH, expand=True)


frm_main = tk.Frame()
vars.setFrmMain(frm_main)
btn_return = tk.Button(master=frm_win, text="Return", height=5, width=35, command=lambda: ops.openScreen(vars.top))
btn_return.pack()

test.start()

ops.openScreen(vars.top)
window.mainloop()
