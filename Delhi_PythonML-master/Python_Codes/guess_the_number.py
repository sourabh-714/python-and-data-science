import random

cpu_num = random.randint(1,100)

#cpu_num = 40

game = True
while game:
    guess = int(input("Guess the number : "))
    if cpu_num == guess:
        print("Congrats, You guessed the number...")
        game = False
    elif cpu_num > guess:
        print("Number is too small")
    elif cpu_num < guess:
        print("Number is too large")
    else:
        print("Invalid Input...Enter a number b/w 1 to 100")
