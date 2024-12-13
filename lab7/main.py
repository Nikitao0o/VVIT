from adw import *

window = Tk()

window.title("Управление персоналом")
window.geometry("1000x1000")

lab = Label(text='Enter new employee name:')
lab.pack()

name = ttk.Entry()
name.pack()
ttk.Button(text='Manager', command=lambda: manag_w(name.get())).pack()
ttk.Button(text="Technician", command=lambda: tech_w(name.get())).pack()
ttk.Button(text="Tech Manager", command=lambda: techm_w(name.get())).pack()
ttk.Button(text="New Employee", command=lambda: employee_w(name.get())).pack()

window.mainloop()
