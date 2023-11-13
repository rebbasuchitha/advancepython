from tkinter import*
root=Tk()
root.title("Demo Application")
root.geometry("500x300+500+300")
root.config(bg="red") 

def bgr():
  root.config(bg="red")
def bgb():
  root.config(bg="blue")
def bgg():
  root.config(bg="green")
b1=Button(text="red", width=20, command=bgr)
b1.pack(pady=20)
b2=Button(text="blue",width=20,command=bgb)
b2.pack(pady=20)
b3=Button(text="green",width=20,command=bgg)
b3.pack(pady=20)
b4=Button(text="quit",width=20,command=quit)
b4.pack(pady=20)
mainloop() 