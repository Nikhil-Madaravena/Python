from tkinter import *

f = Tk()
f.geometry("600x300")
f.title("calculator")

#boundries
b1=Button(f,text="  ")
b2=Button(f,text="  ")
b3=Button(f,text="  ")
b4=Button(f,text="  ")
b5=Button(f,text="  ")
b6=Button(f,text="calculator")
b7=Button(f,text="  ")
b8=Button(f,text="  ")
b1.place(x=0,y=0)
b2.place(x=0,y=500)
b3.place(x=580,y=0)
b4.place(x=580,y=500)
b5.place(x=0,y=250)
b6.place(x=270,y=0)
b7.place(x=580,y=250)
b8.place(x=250,y=500)

# variables
n1 = IntVar()
n2 = IntVar()
n1.set("")
n2.set("")

# labels and text boxes
l_n1 = Label(f, text="Enter first number :")
e_n1 = Entry(f, width=20, textvariable=n1)
l_n1.place(x=50, y=50)
e_n1.place(x=200, y=50)
l_n2 = Label(f, text="Enter second number :")
e_n2 = Entry(f, width=20, textvariable=n2)
l_n2.place(x=50, y=100)
e_n2.place(x=200, y=100)

# Result text box
result_text = Text(f, height=1, width=40, wrap=WORD)
result_text.place(x=50, y=200)

# add def
def add():
    a = n1.get()
    b = n2.get()
    result = f" {a} + {b} = {a + b}"
    result_text.delete(1.0, END)
    result_text.insert(END, result)
    n1.set('')
    n2.set('')

# sub def
def sub():
    a = int(n1.get())
    b = int(n2.get())
    result = f" {a} - {b} = {abs(a - b)}"
    result_text.delete(1.0, END)
    result_text.insert(END, result)
    n1.set('')
    n2.set('')
    
# pro def
def product():
    a = n1.get()
    b = n2.get()
    result = f" {a} * {b} = {a * b}"
    result_text.delete(1.0, END)
    result_text.insert(END, result)
    n1.set(0)
    n2.set(0)

# div def
def div():
    try:
        a = int(n1.get())
        b = int(n2.get())
        if b != 0:
            result = f" {a} / {b} = {a / b}"
            result_text.delete(1.0, END)
            result_text.insert(END, result)
        else:
            result_text.delete(1.0, END)
            result_text.insert(END, "Error: Cannot divide by zero!")
    except ValueError:
        result_text.delete(1.0, END)
        result_text.insert(END, "Invalid input. Please enter valid integers.")


# pow def
def pow():
    a = int(n1.get())
    b = int(n2.get())
    result = f"{a} ^ {b} = {a**b} "
    result_text.delete(1.0,END)
    result_text.insert(END, result)
    n1.set(0)
    n2.set(0)

b_add = Button(f, text="Addition", command=add,activeforeground="black",activebackground='blue',bg="green")
b_add.place(x=20, y=150)
b_sub = Button(f, text="Subtraction", command=sub,activeforeground="black",activebackground='blue',bg="green")
b_sub.place(x=120, y=150)
b_pro = Button(f, text="Product", command=product,activeforeground="black",activebackground='blue',bg="green")
b_pro.place(x=220, y=150)
b_div = Button(f, text="Division", command=div,activeforeground="black",activebackground='blue',bg="green")
b_div.place(x=320, y=150)
b_pow = Button(f, text="Power", command=pow,activeforeground="black",activebackground='blue',bg="green")
b_pow.place(x=420,y=150)
b_goback=Button(f,text="go back",command=f.destroy,bg="orange",activebackground='red')
b_goback.place(x=420,y=250)

f.mainloop()