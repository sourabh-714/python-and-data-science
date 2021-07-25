class Person:
    def __init__(self,occupation):
        self.address = "Delhi"
        self.country = "India"
        self.occupation = occupation

    def checkPerson(self):
        if self.occupation == "Employee":
            print("You can apply for loan")
        elif self.occupation == "Student":
            print("You cannot apply for loan")

class Employee(Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.occupation = "Employee"
        # super is used to call parent class constructor
        super().__init__(self.occupation)

    def showEmp(self):
        print("Name", self.name)
        print("Age", self.age)
        print("Occupation", self.occupation)
        print("Address",self.address, self.country)

class Student(Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.occupation = "Student"
        # super is used to call parent class constructor
        super().__init__(self.occupation)

    def showStudent(self):
        print("Name", self.name)
        print("Age", self.age)
        print("Occupation", self.occupation)
        print("Address",self.address, self.country)
        
emp = Employee("Ram",34)
emp.showEmp()
emp.checkPerson()

student = Student("Ram",34)
student.showStudent()
student.checkPerson()