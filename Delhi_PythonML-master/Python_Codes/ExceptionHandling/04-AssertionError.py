def atm():
    pin = input("Enter your PIN : ")
    total = 10000
    # assert -> AssertionError
    assert (pin == "1234"), "Login Failed"
    print("Login Success")

    amt = int(input("Enter the amount : "))
    assert (total > amt), "Insufficient Balance"
    total -= amt
    print("Transaction completed...")
    print("Remaining balance is",total)

try:
    atm()
except AssertionError as err:
    print(err)
    atm()