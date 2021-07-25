class Emp:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
        self.dept = "IT"
        self.shift = "Morning"
        self.employees = []

    def storeEmp(self):
        self.employees.append([self.id, self.name, self.sal, self.dept, self.shift])

    def showEmp(self):
        print(self.employees)

emp_1 = Emp(101,'Ram',34000)
emp_1.storeEmp()

emp_2 = Emp(102,'Shyam',45000)
emp_2.storeEmp()

# emp_2.showEmp()
print(emp_2)
