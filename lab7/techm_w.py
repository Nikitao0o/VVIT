from tkinter import *
from tkinter import ttk
from emp import *
from tkinter.messagebox import showerror, showinfo, showwarning

def techm_w(name): #TODO: добавить авторизацию по паролю , Починить надоедливое сообщение
    def start(ch, np):
        try:
            ch.start_project(np)
            info = ch.get_info()
            t = f'name {info["name"]} \nid {info["id"]}\ndepartment {info["department"]}\nprojects {info["projects"]}'
            l1.config(text=t)
        except NameTaken:
            showwarning('hey', NameTaken.message)

    def complete(ch, p):
        try:
            ch.complete_project(p)
            info = ch.get_info()
            t = f'name {info["name"]} \nid {info["id"]}\ndepartment {info["department"]}\nprojects {info["projects"]}'
            l1.config(text=t)
        except UndefinedProject:
            showwarning('hey', UndefinedProject.message)

        info = ch.get_info()
        t = f'name {info["name"]} \nid {info["id"]}\ndepartment {info["department"]}\nprojects {info["projects"]}'
        l1.config(text=t)
    id = next(genid())
    ch = TechManager(name=name, id=id)
    techmanagers[id] = ch
    print('techmanagers',techmanagers)
    window = Tk()
    window.title(f'{name} - Tech Manager')
    info = ch.get_info()
    t = f'name {info["name"]} \nid {info["id"]}\nspecification {info["specification"]}\ndepartment {info["department"]}\nprojects {info["projects"]}'
    l1 = ttk.Label(window, text=t)
    l1.pack(anchor='nw')
    new_project = ttk.Entry(window)
    new_project.pack()
    ttk.Button(window, text='start project', command=lambda: start(ch, new_project.get())).pack()
    old_project = ttk.Entry(window)
    old_project.pack()
    ttk.Button(window, text='comlete project', command=lambda: complete(ch, old_project.get())).pack()

    project_name = ttk.Entry(window)
    project_name.pack(anchor='w')
    ttk.Button(window, text='join project', command=lambda: ch.join_project(project_name.get())).pack(anchor='w')
    ttk.Button(window, text='leave project', command=lambda: ch.leave_project(project_name.get())).pack(anchor='w')
    ttk.Button(window, text='check projects', command=lambda: in_projects(ch)).pack(anchor='w')
    l2 = ttk.Label(window, text='-----')
    def in_projects(ch):
        l2.config(text=f'{ch.in_projects()}')
    l2.pack(anchor='w')

    def add_e(ch,project, employee):
        ch.add_employee(project, employee)
        info = str(ch.get_team_info(Project.all_projects[project]))
        l3.config(text=f'team!: {info}')

    def rm_e(ch,project, employee):
        ch.remove_employee(project, employee)
        info = ch.get_team_info(Project.all_projects[project])
        l3.config(text=f'team!: {info}')

    l3 = ttk.Label(window, text=f'team: ')
    l3.pack(anchor='e')
    e3 = ttk.Entry(window)
    ee3 = ttk.Entry(window)
    e3.pack(anchor='e')
    ee3.pack(anchor='e')

    ttk.Button(window, text='add employee', command=lambda: add_e(ch,e3.get(), ee3.get())).pack(anchor='e')
    ttk.Button(window, text='remove employee', command=lambda: rm_e(ch,e3.get(), ee3.get())).pack(anchor='e')
