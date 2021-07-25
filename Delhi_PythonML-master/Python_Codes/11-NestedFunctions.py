def calc():
    x = 10
    y = 11

    def add():
        z = x + y
        return z

    def sub():
        z = x - y
        return z

    return add, sub

# a,b = calc()
# print(a())
# print(b())
a = calc()[0]()
print(a)

b = calc()[1]()
print(b)





