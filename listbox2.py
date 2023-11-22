from tkinter import*
root=Tk()
root.geometry("600x500")
iname=['pen','pencil','book','eraser','scale','bag','ink']
def selitem(evt):
   p=y.get(y.curselection())
   lb1.config(text=p)
y=Listbox(root,width=60,height=10,font=('times',13))
y.bind('<<ListboxSelect>>',selitem)
y.pack()
lb1=Label(width=40,bg="red")
lb1.pack()
for items in iname:
   y.insert(END,items)
root.mainloop()