import tkinter as tk 

import button_operations as button_ops
import operations as ops

import test

def start():
    window = tk.Tk()
    window.title("Mixer")
    window.geometry("800x600")

    # General frame splitting & assigning to larger frames
    frm_win = tk.Frame(master=window)
    frm_win.pack(fill=tk.BOTH, expand=True)


    frm_main = tk.Frame()
    button_ops.setFrmMain(frm_main)
    btn_return = tk.Button(master=frm_win, text="Return", height=5, width=35, command=lambda: ops.openScreen(button_ops.top))
    btn_return.pack()

    test.start()

    button_ops.printAudio()
    ops.openScreen(button_ops.top)
    window.mainloop()
