from tkinter import *
from tkinter.messagebox import showinfo
m=Tk()
m.geometry('180x200')
listbox=Listbox(m,width=40,height=10,selectmode=MULTIPLE)
listbox.insert(1,"ds")
listbox.insert(2,"algorithm")
listbox.insert(3,"data science")
listbox.insert(4,"AI")
def selected_item():
    for i in listbox.curselection():
        showinfo(title='pop up window',
        message=f'selected sub(s):{listbox.get(i)}')
        #print(listbox.get(i))
btn=Button(m,text="print selected",command=selected_item)
btn.pack(side="bottom")
listbox.pack()
m.mainloop()