class Emp:
    employees = []
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
        self.dept = "IT"
        self.shift = "Morning"
        self.current_emp = {}

def main():
    while True:
        print("""
        1. Login
        2. Register
        """)
        choice = input("Enter your choice : ")

