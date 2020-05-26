import pickle
import datetime


def currentDateTime():
    currentDT = datetime.datetime.now()
    return currentDT.strftime("::%H:%M:%S %Y-%m-%d ")

def readData(list,user):
    print(luettu)

def addText(list,user):
    addText = input("Add text: ")
    list.append(addText)

def chngIndexAndWrtNewData(list,user):
    print("In the list is", len(list), "items.")
    changeIndex = int(input("Which index you want to change?: ")) - 1
    changeItem = list[changeIndex]
    print(changeItem,currentDateTime())
    newItem = input("Write new text: ")
    list[changeIndex] = newItem


def deleteIndex(list,user):
    print("In the list is", len(list), "items.")
    deleteIndex = int(input("Which index you want to delete?: "))
    print("Deleted item is: ", list.pop(deleteIndex - 1),currentDateTime())

def operationWithUserInput(listItem,userInput):
    if userInput == 1:
        readData(listItem,userInput)
    elif userInput == 2:
        addText(listItem,userInput)
    elif userInput == 3:
        chngIndexAndWrtNewData(listItem,userInput)
    elif userInput == 4:
        deleteIndex(listItem,userInput)

luettu = []
tiedosto = open("info.txt","rb")
try:
    luettu = pickle.load(tiedosto)
except EOFError:
    print("file is empty")
tiedosto.close()
while True:
    print("""(1) Lue muistikirja
(2) Lisää merkinä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopetta""")
    try:
        numbers = int(input("What do you want?: "))
    except ValueError:
        print("You have written string instead of int.")
        numbers = int(input("What do you want?: "))
    tiedosto = open("info.txt", 'wb')
    if numbers == 5:
        print("Lopettaa")
        break
    else:
        operationWithUserInput(luettu,numbers)

tiedosto = open("info.txt", 'wb')
pickle.dump(luettu,tiedosto)
tiedosto.close()

