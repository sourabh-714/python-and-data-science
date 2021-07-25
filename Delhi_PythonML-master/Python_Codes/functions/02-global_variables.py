# Global variables
y = 10

# Function definition
def add():
    global x
    x = 20
    z = x + y
    print("Sum is",z)

# Function call
add()
diff = x - y
print("Diff is",diff)

x = 50
print("X is",x)
