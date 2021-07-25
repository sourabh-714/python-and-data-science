class Emp:
    # constructor
    def __init__(self):
        self.id = None
        self.name = None
        self.sal = None
        self.dept = "IT"
        self.shift = "Morning"
        self.employees = []

    def storeEmp(self):
        self.employees.append([self.id, self.name, self.sal, self.dept, self.shift])

    def showEmp(self):
        print(self.employees)

emp_1 = Emp()
emp_1.id = 101
emp_1.name = "Ram"
emp_1.sal = 34000
emp_1.storeEmp()

emp_2 = Emp()
emp_2.id = 102
emp_2.name = "Shyam"
emp_2.sal = 39000
emp_2.shift = "Evening"
emp_2.storeEmp()

# emp_2.showEmp()
print(emp_2.employees)