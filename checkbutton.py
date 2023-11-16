from tkinter import*
root=Tk()
root.eval("tk::PlaceWindow . Center")
Checkbutton(text="DCA").grid(row=1,sticky=W)
Checkbutton(text="Java").grid(row=2,sticky=W)
Checkbutton(text="Python").grid(row=3,sticky=W)
mainloop()
