def km_to_m(km):
    return km * 1000

def m_to_km(m):
    return m / 1000

def temp_conv(c):
    return 9/5 * c + 32

# km = 4.56
# m = km_to_m(km)
# print(m)

# kms = [4.33,54.66,1.6,2.8]
# ms = []
# for item in kms:
#     ms.append(km_to_m(item))
# print(ms)
#
# temps = [34.55,45.33,38.76,31.45,38.77]
# f = []
# for item in temps:
#     f.append(temp_conv(item))
# print(f)

def myMap(func, iter):
    data = []
    for i in range(len(iter)):
        data.append(func(iter[i]))
    return data

temps = [34.55,45.33,38.76,31.45,38.77]
f = myMap(temp_conv, temps)
print(f)

kms = [4.33,54.66,1.6,2.8]
ms = myMap(km_to_m, kms)
print(ms)
