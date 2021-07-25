login = True

def loginNow():
    email = input("Enter email : ")
    pwd = input("Enter pwd : ")

def check_login(func) -> "will always return a function":
    def loginUser():
        if login:
            print("Already logged in...")
            func()
        else:
            print("Login First")
            loginNow()
            print("Login Success...")
            func()
    return loginUser

@check_login
def comment():
    p = input("Enter your comment : ")
    print("Your comment : ",p)

# comment()
# x = check_login(comment)
# x()

@check_login
def subscribe():
    print("Subscribed Successfully...")

@check_login
def like():
    print("Added to liked videos")

@check_login
def reply_comment():
    reply = input("Enter reply : ")
    print("Reply :",reply)

# comment()
# subscribe()
# like()
reply_comment()
