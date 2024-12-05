class Employee:
    def __init__(self, id, name):
        self.name = name
        self.id = id
    def get_info(self):
        return self.name, self.id
    
class Manager(Employee):
    def __init__(self, id, name, department):
        Employee.__init__(self, id, name)
        self.department = department
    def manage_project(self):
        return 'managing_project'
    def get_info(self):
        return self.name, self.id, self.department
        
class Technician(Employee):
    def __init__(self, id, name, specialization):
        Employee.__init__(self, id, name)
        self.specialization = specialization
    def perform_maintenance(self):
        return 'da'
    def get_info(self):
        return self.name, self.id, self.specialization

class TechManager(Manager, Technician):
    def __init__(self, id, name, department, specialization):
        Manager.__init__(self, id, name, department)   
        Technician.__init__(self, id, name, specialization)
        self.employee = [self]
    def manage_project(self):
        return Manager.manage_project()
    
    def perform_maintenance(self):
        return Technician.perform_maintenance()
    
    def get_info(self):
        return self.name, self.id, self.department, self.specialization
    
    def add_employee(self, new_emp):
        self.employee.append(new_emp)
    def get_team_info(self):
        return [emp.get_info() for emp in self.employee]
    
a = TechManager('1', 'loh', 'IT', 'Networking')
emp1 = Manager('2', 'loshara','ads')
emp2 = Employee('3', 'petux')
a.add_employee(emp1)
a.add_employee(emp2)
print(a.get_team_info())
emp3 = Technician('4','xz','da')
print(emp1.manage_project())
print(emp3.perform_maintenance())