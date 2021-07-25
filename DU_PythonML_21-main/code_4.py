import random

cpu = random.randint(1,100)

count = 0
game = True
while game:
    guess = int(input("Enter your guess : "))
    if cpu == guess:
        print("Congrats, you guessed the number")
        game = False
    elif cpu > guess:
        print("Number is smaller")
    elif cpu < guess:
        print("Number is larger")

    count += 1
    if count == 5:
        print("Game Over, You lose, Number was",cpu)
        game = False




