import math

def add(luku1,luku2):
    return luku1 + luku2

def subtract(luku1,luku2):
    return luku1 - luku2

def multiply(luku1,luku2):
    return luku1 * luku2

def divide(luku1,luku2):
    return luku1 / luku2

def trigoSin(luku1,luku2):
    return math.sin(luku1 / luku2)

def trigoCos(luku1,luku2):
    return math.cos(luku1 / luku2)

def takeInput(word=""):
    incorrectInput = True
    while incorrectInput:
        user = userInput(word)
        if user:
            incorrectInput = False
    return user

def userInput(word):
    if (len(word)>0):
        word = " " + word
    try:
        muttuja1 = int(input("Anna" + word + " ensimmäinen luku: "))
        muttuja2 = int(input("Anna" + word + " toinen luku: "))
        return (muttuja1,muttuja2)
    except ValueError:
        print("Please enter numeric data only")
        return None