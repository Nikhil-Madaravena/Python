import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
m = tk.Tk()
m.geometry("300x250")
m.title("combobox")
l = ttk.Label(text="please select the month")
l.pack(fill=tk.X, padx=5, pady=5)
selec_month = tk.StringVar()
month_cb = ttk.Combobox(m, textvariable=selec_month)
month_cb['value'] = [month_name[i][:9] for i in range(1, 13)]
month_cb['state'] = 'readonly'
month_cb.pack(fill=tk.X, padx=5, pady=5)
def month_change(event):
    showinfo(
        title='pop up window',
        message=f'you have selected a month: {selec_month.get()}!')
month_cb.bind('<<ComboboxSelected>>', month_change)
m.mainloop()