from tkinter import *
m=Tk()
m.geometry("450x300")
m.title("user interface")
name_var =StringVar()
passw_var = StringVar()
name1 = "Nikhil"
password1 = "2006"
i = 1
def submit():
    global i
    name=name_var.get()
    password=passw_var.get()
    if name == name1 and password == password1:
        print("you logged in:")
    else:
        print("something went wrong check details")
        print("you are left with {i}th attempts")
        print("still you left with{3-i} attempts only")
        i+=1
        if i==4:
            print("you finished your attempts")
            m.destroy()
        else:
            print("enter your username and password again")
    name_var.set(" ")
    passw_var.set(" ")
l1=Label(m,text="username")
l2=Label(m,text="password")
t1=Entry(m,width=30,textvariable=name_var)
t2=Entry(m,width=30,textvariable=passw_var,show="*")
b1=Button(m,text="log in",command=submit)
l1.grid(row=0,column=0,pady=2)
t1.grid(row=0,column=1,pady=2)
l2.grid(row=1,column=0,pady=2)
t2.grid(row=1,column=1,pady=2)
b1.grid(row=2,column=0,pady=2)
m.mainloop()