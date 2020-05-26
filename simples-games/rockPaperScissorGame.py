import random
countOfRounds = 0
countOfUserWins = 0
while True:
    print("""(1) Rock
(2) Paper
(3) Scissor""")
    lista = {1: "Rock",
             2: "Paper",
             3: "Scissor"}
    userInput = int(input("Choose 1 no.(1-3): "))
    if userInput not in range(1,4):
        print("Game finnish!!")
        break
    print("You have choosen:",lista.get(userInput))
    computer = random.randint(1, 3)
    print("computer has choosen:",lista.get(computer))
    countOfRounds += 1

    if userInput == computer:
        print("Draw!!")
    elif (userInput == 1 and computer == 3) or (userInput == 3 and computer == 2) or(userInput == 2 and computer == 1):
        print("You have won.")
        countOfUserWins += 1
    else:
        print("Computer won.")
print(countOfRounds, "times user played game and", countOfUserWins, "times user have won game.")