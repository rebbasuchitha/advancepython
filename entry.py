from tkinter import*
root=Tk()
root.title("Demo Application")
root.geometry("500x300+500+300")
root.config(bg="red")
e1=Entry()
e1.pack()
e2=Entry()
e2.insert(0,'Nipuna Technologies')
e2.pack()

mainloop()