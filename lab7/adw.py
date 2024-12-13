from tkinter import *
from tkinter import ttk
from emp import *
from tkinter.messagebox import showerror, showinfo, showwarning
from techm_w import *
from manag_w import *
from tech_w import *


def employee_w(name):
    id = next(genid())
    ch = Employee(name=name, id=id)
    employees[id] = ch
    print('employees',employees)
    window = Tk()
    window.title(f'{name} - Employee')
    info = ch.get_info()
    t = f'name {info["name"]} \nid {info["id"]}'
    l1 = ttk.Label(window, text=t)
    l1.pack(anchor='nw')

    ttk.Label(window, text='Иди Работай', font=('Arial', 36)).pack(anchor='center')
