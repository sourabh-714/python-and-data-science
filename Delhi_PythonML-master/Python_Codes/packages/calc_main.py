import calc_logic

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = input("Enter your choice : ")

f_num = int(input("Enter first number : "))
s_num = int(input("Enter second number : "))

operations = {
    "1" : calc_logic.add,
    "2" : calc_logic.sub,
    "3" : calc_logic.div,
    "4" : calc_logic.mul
}

output = operations.get(ch)(f_num, s_num)
print("Result is",output)
