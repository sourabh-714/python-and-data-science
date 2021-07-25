def even(n):
    return n % 2 == 0

def odd(n):
    return n % 2 != 0

numbers = [45,44,6,23,26,41,27,31,56,88,91]

def myFilter(func, iter):
    data = [iter[i] for i in range(len(iter)) if func(iter[i])]
    return data

e = myFilter(even, numbers)
o = myFilter(odd, numbers)
print(e)
print(o)
