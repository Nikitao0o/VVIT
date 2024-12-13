from tkinter import *
from tkinter import ttk
from emp import *
from tkinter.messagebox import showerror, showinfo, showwarning

def manag_w(name): #TODO: добавить авторизацию по паролю
    def start(ch, np):
        ch.start_project(np)
        info = ch.get_info()
        t = f'name {info["name"]} \nid {info["id"]}\ndepartment {info["department"]}\nprojects {info["projects"]}'
        l1.config(text=t)

    def complete(ch, p):
        try:
            ch.complete_project(p)
            info = ch.get_info()
            t = f'name {info["name"]} \nid {info["id"]}\ndepartment {info["department"]}\nprojects {info["projects"]}'
            l1.config(text=t)
        except UndefinedProject:
            showwarning('hey', 'There is no such project')

        info = ch.get_info()
        t = f'name {info["name"]} \nid {info["id"]}\ndepartment {info["department"]}\nprojects {info["projects"]}'
        l1.config(text=t)
    id = next(genid())
    ch = Manager(name=name, id=id)
    managers[id] = ch
    print('managers', managers)
    window = Tk()
    window.title(f'{name} - Manager')
    info = ch.get_info()
    t = f'name {info["name"]} \nid {info["id"]}\ndepartment {info["department"]}\nprojects {info["projects"]}'
    l1 = ttk.Label(window, text=t)
    l1.pack(anchor='nw')
    new_project = ttk.Entry(window)
    new_project.pack()
    ttk.Button(window, text='start project', command=lambda: start(ch, new_project.get())).pack()
    old_project = ttk.Entry(window)
    old_project.pack()
    ttk.Button(window, text='comlete project', command=lambda: complete(ch, old_project.get())).pack()
