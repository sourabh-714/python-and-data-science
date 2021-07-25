# variable length arguments
# *args
def add(*x):
    z = 0
    for i in range(len(x)):
        z += x[i]
    print("Sum is",z)

add(5,4)
add(5,4,6,3)
add(4,5,6,8,3,4,5)
add(4,5,6,54,4,5,7,87,8,6)
