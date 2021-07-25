try:
    a = int(input("Enter first num : "))
    b = int(input("Enter second num : "))
    c = a + b
    d = a - b
    e = a / b
    f = a * b
except ZeroDivisionError:
    print("Cannot Divide by Zero...")
# except ArithmeticError as err:
#     print(err)
except ValueError:
    print("Invalid Input...Please enter a digit")
except BaseException as err:
    print(err)
else:
    print("Sum is", c)
    print("Sub is", d)
    print("Div is", e)
    print("Mul is", f)