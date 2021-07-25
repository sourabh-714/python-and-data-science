numbers = [45,44,6,23,26,41,27,31,56,88,91]

e = list(map(lambda x : x % 2 == 0, numbers))
# o = list(filter(lambda x : x % 2 != 0, numbers))
# print(o)

print(e)