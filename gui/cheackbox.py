from tkinter import *
m = Tk()
m.geometry("300x300")
m.title("edit box")
w=Label(m,text='programming languages',font=50)
w.pack()
Checkbutton1=IntVar()
Checkbutton2=IntVar()
Checkbutton3=IntVar()

cb1=Checkbutton(m,text='python',    
    variable=Checkbutton1,
    onvalue=1,
    offvalue=0,
    height=5,
    width=10)
cb2=Checkbutton(m,text='java',    
    variable=Checkbutton2,
    onvalue=1,
    offvalue=0,
    height=5,
    width=10)
cb3=Checkbutton(m,text='c',    
    variable=Checkbutton3,
    onvalue=1,
    offvalue=0,
    height=5,
    width=10)
cb1.pack()
cb2.pack()
cb3.pack()
m.mainloop()