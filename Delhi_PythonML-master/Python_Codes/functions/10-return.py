# def sayHello():
    # print("Hello User")
    # return "Hello User"

# msg = sayHello()
# print(msg)

def calc(x,y):
    z1 = x + y
    z2 = x - y
    z3 = x / y
    z4 = x * y
    return z1,z2,z3,z4

# z = calc(4,5)
# print(z)

# Packing & Unpacking
a,b,c,d = calc(4,5)
print(a,b,c,d)
