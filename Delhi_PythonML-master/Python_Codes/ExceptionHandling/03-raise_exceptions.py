def atm():
    pin = input("Enter your PIN : ")
    total = 10000
    if pin == "1234":
        print("Login Success")
    else:
        raise ValueError("Login Failed")

    amt = int(input("Enter the amount : "))
    if total < amt:
        raise ValueError("Insufficient Balance")
    else:
        total -= amt
        print("Transaction completed...")
        print("Remaining balance is",total)

try:
    atm()
except ValueError as err:
    print(err)
    atm()