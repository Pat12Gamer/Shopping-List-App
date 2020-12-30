import sys

shopping_list = []# shopping list

# Clear the main menu
def mainMenu():
    while True:
        print()
        print('''### SHOPPING LIST ###

        Select a number for the action that you would like to do:

        1. View shopping list
        2. Add item to shopping list
        3. Remove item from shopping list
        4. Check if item is on shopping list
        5. How many items on shopping list
        6. Clear Shopping list
        7. Exit
        ''')

        selection = input("make your selection: ") # Ask the user to make a selection

        if selection == "1":
            displayList()
        elif selection == "2":
            addItem()
        elif selection == "3":
            removeItem()
        elif selection == "4":
            checkItem()
        elif selection == "5":
            listLength()
        elif selection == "6":
            clearList()
        elif selection == "7":
            sys.exit()
        else:
            print("You did not make a valid selection")

def displayList():
    if len(shopping_list) >= 1:
        print()
        print("### SHOPPING LIST ###")
        for i in shopping_list:
            print("* " + i)
    else:
        print('''
        There are no items in the list
        ''')

def addItem():
    s="#"
    while True:
        item = (str(input("Enter an item and press the enter key to continue adding an item. Type # and press enter key if you wish to stop ")))
        shopping_list.append(item)
        if s in item:
            shopping_list.remove("#")
            break

def removeItem():
    item = input("What item would you like to remove from the shopping list: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(item + " has been removed from to your list.")
    else:
        print("This item is not in your list")

def checkItem():
    item = input("What item would you like to check on the shopping list: ")
    if item in shopping_list:
        print("Yes, " + item + " that item is on the shopping list.")
    else:
        print("No, " + item + " that item is not on the shopping list.")

def listLength():
    print("There are ", len(shopping_list), " items on the list")

def clearList():
    shopping_list.clear()
    print("The shopping list is now empty.")

mainMenu()
