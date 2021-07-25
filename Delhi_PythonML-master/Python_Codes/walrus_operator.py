a = 12
b = 22

# walrus operator
#print("Sum is",c := a + b)

#print(f"Sum of {a=} and {b=} is {c=}")

#print(f"Sum of {a=} and {b=} is {(c:=a+b)}")

print(f"""
1. Sum is {(c := a + b)}
2. Sub is {(c := a - b)}
3. Div is {(c := a / b)}
4. Mul is {(c := a * b)}
""")
