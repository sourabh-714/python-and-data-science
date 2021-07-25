def km_to_m(km):return km * 1000

def m_to_km(m):return m / 1000

def temp_conv(c):return 9/5 * c + 32

temps = [34.55,45.33,38.76,31.45,38.77]
f = list(map(temp_conv, temps))
print(f)

kms = [4.33,54.66,1.6,2.8]
ms = list(map(km_to_m, kms))
print(ms)
