import  tkinter as tk
from tkinter import*
from tkinter import ttk
root=Tk()
root.geometry("300x150")
def my_upd(*args):
 l1.config(text=sel.get())
sel=tk.StringVar()
months=['Jan','Feb','March','Apr','May','Jun']
cb1=ttk.Combobox(root,values=months,width=7,textvariable=sel)
cb1.grid(row=1,column=1,padx=10,pady=20)
cb1.current(5)
l1=Label(root,text=' ')
l1.grid(row=1,column=2)
sel.trace('w',my_upd)
mainloop()