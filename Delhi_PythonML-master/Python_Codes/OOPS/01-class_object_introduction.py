class Emp:
    id = None
    name = None
    sal = None
    dept = "IT"
    shift = "Morning"

emp_1 = Emp()
emp_1.id = 101
emp_1.name = "Ram"
emp_1.sal = 34000
print("Emp-1",emp_1.name, emp_1.sal, emp_1.shift)

emp_2 = Emp()
emp_2.id = 102
emp_2.name = "Shyam"
emp_2.sal = 39000
print("Emp-2",emp_2.name, emp_2.sal, emp_2.shift)
