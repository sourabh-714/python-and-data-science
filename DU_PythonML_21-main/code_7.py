from datetime import datetime as dt

helloIntent = ["hi","hey","hello","hi there"]
dateIntent = ["date","tell me date","what's the date"]
timeIntent = ["time","tell me time","what's the time"]

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg in helloIntent:
        print("Hello User")

    elif msg in dateIntent:
        current_date = dt.now().date()
        print(current_date.strftime('%d/%m/%y, %a'))

    elif msg in timeIntent:
        current_time = dt.now().time()
        print(current_time.strftime("%H:%M:%S, %p"))
        
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
