import random

highest = 100
answer = random.randint(1, highest)
print("Please guess a number between 1 and {}: ".format(highest))
guess =  0

while guess != answer:
    guess = int(input())

    if guess < answer:
        print("Guess higher")
    elif guess > answer:
        print("Guess lower")
    else:
        print("You guessed it")