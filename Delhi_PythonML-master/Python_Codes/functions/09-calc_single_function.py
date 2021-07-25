def calc(x,y,opr):
    expression = x + opr + y
    result = eval(expression)
    print(expression,'=',result)

print("""
1. Add
2. Sub
3. Mul
4. Div
""")

ch = input("Enter your choice : ")
num_1 = input("Enter first number : ")
num_2 = input("Enter second number : ")

opr = {
    "1" : "+",
    "2" : "-",
    "3" : "*",
    "4" : "/"
}
operator = opr.get(ch)
calc(num_1, num_2, operator)
