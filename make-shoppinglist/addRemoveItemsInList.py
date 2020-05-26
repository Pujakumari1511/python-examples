def takeOperationInputFromUser():
    try:
        selectNo = int(input("ChoseNo between 1-3: "))
        return selectNo
    except ValueError:
        print("You have written string instead of int.")

def takeItemInputFromUser(message):
    inputItem = input(message)
    item = inputItem[0].upper() + (inputItem[1:].lower() if len(inputItem) > 1 else "")
    return item

def printListOfItems(list):
    print("The current items in shopping list are:\n", ", ".join(list))

def addItem(listOfItem):
    printListOfItems(listOfItem)
    print("what do you want to add in list: ")
    listOfItem.append(takeItemInputFromUser("Add an item: "))
    printListOfItems(listOfItem)

def removeItem(listOfItem):
    print("Listalla on", len(listOfItem), "alkiota")
    printListOfItems(listOfItem)
    deleteItem = takeItemInputFromUser("Which item you want to remove?: ")
    if deleteItem not in listOfItem:
        print("This item {} is not in your list.".format(deleteItem))
    else:
        listOfItem.remove(deleteItem)
        print('Item "{}" removed for the list.'.format(deleteItem))
        printListOfItems(listOfItem)

def createDict():
    func_dict = {
        1: addItem,
        2: removeItem,
        3: printListOfItems
    }
    return func_dict

# def addOrRemoveItemInList(chooseNo, shoppinglist):
#     if chooseNo == 1:
#         addItem(shoppinglist)
#     elif chooseNo == 2:
#         removeItem(shoppinglist)
#     else:
#         print("Virhellinen valinta.")

lista = ["Clothes", "Grocerry", "Makeup", "Shoes"]
function = createDict()
while True:
    print("""(1) Lisätä listaan
(2) Poista listalta
(3) Loppettaa""")
    number = takeOperationInputFromUser()
    if number:
        function[number](lista) if number in function.keys() else print("Virhellinen valinta.")
        # if number in function.keys():
        #     function[number](lista)
        # else:
        #     print("Virhellinen valinta.")
        if number==3:
            break
        #addOrRemoveItemInList(number, lista)