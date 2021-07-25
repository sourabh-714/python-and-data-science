def add(x,y):
    z = x + y
    print("Sum is",z)

def sub(x,y):
    z = x - y
    print("Sub is",z)

def mul(x,y):
    z = x * y
    print("Mul is",z)

def div(x,y):
    z = x / y
    print("Div is",z)

print("""
1. Add
2. Sub
3. Mul
4. Div
""")

ch = input("Enter your choice : ")
num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

operations = {
    "1" : add,
    "2" : sub,
    "3" : mul,
    "4" : div
}

operations.get(ch)(num_1, num_2)

