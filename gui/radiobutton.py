from tkinter import *
m = Tk()
m.geometry("300x300")
r=IntVar()
lb1=Label(m,text="what is your gender?")
lb1.pack()

def sel():
    gen="you are a"+str(r.get())
    label.config(text=gen)


r1=Radiobutton(m,text="male",variable=r,value=1,command=sel)
r1.pack(anchor=W)
r2=Radiobutton(m,text="female",variable=r,value=1,command=sel)
r2.pack(anchor=W)
r3=Radiobutton(m,text="other",variable=r,value=1,command=sel)
r3.pack(anchor=W)
label=Label(m)
label.pack()
m.mainloop()





