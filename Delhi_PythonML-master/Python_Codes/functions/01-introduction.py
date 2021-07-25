# Global variables
x = 5
y = 10

# Function definition
def add():
    # local variables
    x = 12
    y = 22
    z = x + y
    print("Sum is",z)

# Function call
add()
z = x - y
print("Diff is",z)
