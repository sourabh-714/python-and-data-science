import read_write_operations

# users = []

def login():
    email = input("Enter email : ")
    pwd = input("Enter password : ")
    users = read_write_operations.read_users()

def register():
    name = input("Enter name : ")
    email = input("Enter email : ")
    pwd = input("Enter password : ")
    city = input("Enter city : ")
    data = {"name":name, "email":email, "pwd":pwd, "city" : city}
    read_write_operations.write_user(data)

def main():
    print("""
    1. Login
    2. Register
    """)
    choice = input("Enter your choice : ")

main()
