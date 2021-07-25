a = 5
b = 6

'''
c = a + b
print("Sum is",c)
'''

#walrus operator
#print("Sum is",c := a + b)

#print(f"Sum of {a} and {b} is {(c := a + b)}")

print(f"""
1. Sum is {(c := a + b)}
2. Sub is {(d := a - b)}
3. Div is {(e := a / b)}
4. Mul is {(f := a * b)}
""")







