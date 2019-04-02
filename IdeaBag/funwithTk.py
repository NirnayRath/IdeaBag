# Some fun activity with tkinter..

import tkinter as tk


master=tk.Tk()



tk.Label(master,text="First name:").grid(row=0,column=0)
tk.Label(master,text="Last name:").grid(row=1,column=0)
f = tk.Entry(master)
f.grid(row=0,column=1)
l = tk.Entry(master)
l.grid(row=1,column=1)


def show():
    tk.Label(master,text=(f.get(),l.get())).grid(row=4,column=0)

tk.Button(master,text="Quit",command=master.quit).grid(row=3,column=0)
tk.Button(master,text="Show",command=show).grid(row=3,column=1)

master.mainloop()