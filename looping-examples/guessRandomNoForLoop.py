import random
highest = 100
print("Please guess number between 1-{}: ".format(highest))
guess = 0
answer = random.randint(1,highest)
countOfNumber = 0
for i in range(1,answer):
    guess = int(input())
    if guess == 0:
        print("You Quit the game")
        break
    elif guess < i:
        print("guess higher")
    elif guess > i:
        print("Guess lower")
    else:
        print("You guessed it")
    countOfNumber += 1
    if countOfNumber == 10:
        print("Sorry,You missed the chance")
        break