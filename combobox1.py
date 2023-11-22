from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry('200x100')
course=["Java","Python","C&c++"]
cb=ttk.Combobox(values=course,width=10)
cb.grid(column=0,row=1)
cb.current(1)
mainloop()