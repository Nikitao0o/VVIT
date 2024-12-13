class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def __get__(self):
        return (self.id, self.name)
    
    x = property(__get__)
    

class Manager(Employee):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.department = None
    def manage_project(self):
        pass

class Technician(Employee):
    def __init__(self, name, id):
        super.__init__(name, id)
        self.specialisation = None
    
    def manage_project(self):
        pass

class TechManager(Technician, Manager):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.department = None
        self.scpecification = None
        self.employees = []

    def add_employee(self, emloyee):
        self.employees.append(employee)
    
    def get_team_info(self):
        return self.employees
