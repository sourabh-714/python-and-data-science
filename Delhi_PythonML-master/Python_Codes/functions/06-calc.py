def calc(*num, **operation):
    values = operation.values()
    if 'add' in values:
        z = 0
        for i in range(len(num)):
            z += num[i]
        print("Sum is",z)
    if 'sub' in values:
        z = 0
        for i in range(len(num)):
            z -= num[i]
        print("Diff is",z)
    if 'mul' in values:
        z = 1
        for i in range(len(num)):
            z *= num[i]
        print("Mul is",z)

calc(4,5,6, opr1 = 'add', opr2 = 'sub')
