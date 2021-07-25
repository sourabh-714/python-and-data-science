# while True:
#     msg = input("Enter your message : ")
#     if msg == "hello":
#         print("Hello User")
#     elif msg == "bye":
#         print("Bye User")
#         break
#     else:
#         print("I don't understand")

while (msg := input("Enter your message : ")) != "bye":
    if msg == "hello":
        print("Hello User")
    else:
        print("I don't understand")
