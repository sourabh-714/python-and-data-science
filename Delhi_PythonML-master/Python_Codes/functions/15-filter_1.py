def even(n):
    return n % 2 == 0

# print(even(103))
# print(even(102))

numbers = [45,44,6,23,26,41,27,31,56,88,91]

# e = []
# for i in range(len(numbers)):
#     if even(numbers[i]):
#         e.append(numbers[i])
# print(e)

e = [numbers[i] for i in range(len(numbers)) if even(i)]
print(e)
