import calculatorSubFunction
while True:
    try:
         userInput = calculatorSubFunction.takeInput()
    except Exception:
        print("Virhellinen syöte!!")
        continue

    numero = 0
    while numero != 8:
        print("""(1) +
(2) -
(3) *
(4) /
(5) sin(muttuja1 / muttuja2)
(6) cos(muttuja1 / muttuja2)
(7) Vaihda luvut
(8) Lopeta""")
        print("Valitut luvut:", userInput[0], userInput[1])
        numero = int(input("Valitse numero(1-8): "))

        if numero == 1:
            print("Tulos on: ", calculatorSubFunction.add(userInput[0], userInput[1]))
        elif numero == 2:
            print("Tulos on: ", calculatorSubFunction.subtract(userInput[0], userInput[1]))
        elif numero == 3:
            print("Tulos on: ", calculatorSubFunction.multiply(userInput[0], userInput[1]))
        elif numero == 4:
            try:
                print("Tulos on: ", calculatorSubFunction.divide(userInput[0], userInput[1]))
            except ZeroDivisionError:
                print("Cannot divide by zero")
        elif numero == 5:
            print("Tulos on: ", calculatorSubFunction.trigoSin(userInput[0], userInput[1]))
        elif numero == 6:
            print("Tulos on: ", calculatorSubFunction.trigoCos(userInput[0], userInput[1]))
        elif numero == 7:
            userInput = calculatorSubFunction.takeInput("uusi")
        else:
            if numero not in range(1,8):
                print("Lopeta")
                break