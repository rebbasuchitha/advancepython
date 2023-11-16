from tkinter import*
root=Tk()
root.title('My Window')
root.geometry('250x100')

var1=IntVar()
var2=IntVar()
l=Label(bg='white',width=20,text='  ')
l.grid(row=3,column=1)

def print_selection():
   if(var1.get()==1)&(var2.get()==0):
      l.config(text='I Love PYTHON')
   elif(var1.get()==0)&(var2.get()==0):
      l.config(text='  ')
   elif(var1.get()==0)&(var2.get()==1):
      l.config(text='I Love HTML')
   elif(var1.get()==0)&(var2.get()==0):
     l.config(text='  ')
   elif(var1.get()==1)&(var2.get()==1):
      l.config(text='I Love both')
c1=Checkbutton(text='python',variable=var1,onvalue=1,offvalue=0,command=print_selection)
c1.grid(row=0,column=0,sticky=W)

c2=Checkbutton(text='html',variable=var2,onvalue=1,offvalue=0,command=print_selection)
c2.grid(row=1,column=0,sticky=W)
mainloop()