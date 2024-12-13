from tkinter import *
from tkinter import ttk
from emp import *
from tkinter.messagebox import showerror, showinfo, showwarning

def tech_w(name): #TODO: добавить авторизацию по паролю
    id = next(genid())
    ch = Technician(name=name, id=id)
    technicians[id] = ch
    print('technicians',technicians)
    window = Tk()
    window.title(f'{name} - Technician')
    info = ch.get_info()
    t = f'name {info["name"]} \nid {info["id"]}\nspecification {info["specification"]}'
    ttk.Label(window, text=t).pack(anchor='nw')
    project_name = ttk.Entry(window)
    project_name.pack()
    ttk.Button(window, text='join project', command=lambda: ch.join_project(project_name.get())).pack()
    ttk.Button(window, text='leave project', command=lambda: ch.leave_project(project_name.get())).pack()
    ttk.Button(window, text='check projects', command=lambda: in_projects(ch)).pack()
    l2 = ttk.Label(window, text='-----')
    def in_projects(ch):
        l2.config(text=f'{ch.in_projects()}')
    l2.pack()
