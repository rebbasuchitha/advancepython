from tkinter import*
from tkinter.ttk import*
root=Tk()
root.title("welcome to app")
rad1=Radiobutton(text='CASH',value="cash")
rad2=Radiobutton(text='CHEQUE',value="cheque")
rad3=Radiobutton(text='DD',value="dd")
rad1.grid(column=0,row=0)
rad2.grid(column=1,row=0)
rad3.grid(column=2,row=0)
mainloop()