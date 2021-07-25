# by default python takes input in string
##name = input("Enter your name : ")
##print("Hello",name)

print("Hello",name := input("Enter your name : "))

# we need to type cast input funtion
x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
z = x + y
print("Sum is",z)
