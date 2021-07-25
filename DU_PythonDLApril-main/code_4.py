#Guess the number game
import random

cpu = random.randint(1,100)

count = 0
game = True
while game:
    guess = int(input("Enter your guess : "))
    if cpu == guess:
        print("You guess the number right...")
        game = False
    elif cpu < guess:
        print("You guessed a larger number")
    elif cpu > guess:
        print("You guessed a smaller number")

    count += 1
    if count == 5:
        print("You lose the game...")
        print("Number was",cpu)
        game = False


