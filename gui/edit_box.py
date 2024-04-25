from tkinter import *
m = Tk()
m.geometry("300x300")
m.title("edit box")
from tkinter import *

m = Tk()
m.geometry("450x300")
m.title("User Interface")

s1c = "nikhil"
s2c = "12345"

s1 = StringVar()
s2 = StringVar()
j=1
def che():
    global j
    un = s1.get()
    p = s2.get()
    if un == s1c and p == s2c:
        print("You have successfully logged in")
        mes="You have successfully logged in"
        l3.config(text=mes)
    else:
        print("Something may be wrong with your entries")
        print(f"This is your {j}th attempt")
        print(f"You have {3-j} attempts left")
        mes1="This is your"
        mes2=str(j)
        mes3="th attempt"
        mes4="You have "
        mes5=str(3-j)
        mes6=" attempts left"
        t1.config(text=mes1+mes2+mes3+mes4+mes5+mes6)
        pass
        pass
        pass
        j+=1
        if j==4:
            print("you are done with your attempts")
            mes7="you are done with your attempts"
            l3.config(text=mes7)
            pass
            pass
            pass
            m.destroy()
    s1.set("")
    s2.set('')

# the label for username
l1 = Label(m, text="Username")
# the label for user password
l2 = Label(m, text="Password")
l3=Label(m,text='')
t1 = Entry(m, width=30, textvariable=s1)
t2 = Entry(m, width=30, show="*", textvariable=s2)

b1 = Button(m, text="Log in", command=che)

l1.place(x=40, y=60)
t1.place(x=110, y=60)
l2.place(x=40, y=100)
t2.place(x=110, y=100)
b1.place(x=40, y=130)
l3.place(x=40,y=160)
m.mainloop()
