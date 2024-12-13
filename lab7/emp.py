from exc import *
from genid import genid

class Projects():
    all_projects = {}

class Project(Projects):
    def __init__(self, name):
        self.__name = name
        self.__status = None
        self.__employees = []
        super().all_projects[f'{name}'] = self

    def name(self):
        return self.__name

    def employees(self):
        return self.__employees

    def add_employee(self, employee_id):
        self.__employees.append(employee_id)

    def remove_employee(self, employee_id):
        self.__employees.pop(self.__employees.index(employee_id))

    def start(self):
        self.__status = "started"

    def complite(self):
        self.__status = "complite"

    def status(self):
        return self.__status

class Employee():
    def __init__(self, name=None, id=None):
        self._name = name
        self._id = id

    def get_info(self):
        return {"name":self._name, 'id':self._id}

class Manager(Employee):
    def __init__(self, name=None,id=None, department=None):
        super().__init__(name, id)
        self._department = department
        self._projects = []
        self.__password = '' # TODO: make password verification

    def get_info(self):
        return {"name":self._name, 'id':self._id, 'department':self._department, 'projects':self._projects}

    def start_project(self, name):
        try:
            if name in Projects.all_projects.keys():
                raise NameTaken
            new_project = Project(name)
            new_project.start()
            self._projects.append(new_project.name())
            print(name, 'started', Projects.all_projects)
        except NameTaken:
            return 0

    def complete_project(self, project):
        try:
            Projects.all_projects[project].complite()
            self._projects.pop(self._projects.index(project))
        except ValueError:
            raise UndefinedProject
        except KeyError:
            raise UndefinedProject

class Technician(Employee):
    def __init__(self, name=None,id=None, specification=None):
        super().__init__(name,id)
        self._specification = specification
        self.__password = '' # TODO: make password verification

    def get_info(self):
        return {"name":self._name, 'id':self._id, 'specification':self._specification}

    def join_project(self, project):
        me = self.get_info()['id']
        if me not in Project.all_projects[project].employees():
            Project.all_projects[project].add_employee(me)
        # print(me,'inpr', Project.all_projects[project].employees())

    def leave_project(self, project):
        me = self.get_info()['id']
        if me in Project.all_projects[project].employees():
            Project.all_projects[project].remove_employee(me)

    def in_projects(self):
        r = []
        for i in Project.all_projects.values():
            if self.get_info()['id'] in i.employees():
                r.append(i.name())
        return r


class TechManager(Manager, Technician):
    def __init__(self, name=None,id=None, specification=None, department=None):
        super().__init__(name,id)
        self._specification=specification
        self._department=department
        self._projects = []
        self.__password = '' # TODO: make password verification

    def get_info(self):
        return {"name":self._name, 'id':self._id, 'specification':self._specification, 'department':self._department, 'projects':self._projects}

    def join_project(self, project):
        return super().join_project(project)

    def leave_project(self, project):
        return super().leave_project(project)

    def in_projects(self):
        return super().in_projects()

    def start_project(self, project):
        return super().start_project(project)

    def complete_project(self, project):
        return super().complete_project(project)

    def add_employee(self, project, employee_id):
        Projects.all_projects[project].add_employee( employee_id)

    def remove_employee(self, project, employee_id):
        Projects.all_projects[project].remove_employee(employee_id)

    def get_team_info(self, project):
        return project.employees()

managers = {}
technicians = {}
techmanagers = {}
employees = {}
