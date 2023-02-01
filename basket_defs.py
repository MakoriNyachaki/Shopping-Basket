cart = {} # Empty dictionary

def selectOption():
    try:
        option = int(input("Enter an option: "))
        return option
    except ValueError:
        pass
        # print("Enter a valid integer!")

def addItem():
    item = input("Enter item:").title()
    try:
        qty = int(input("Enter the quantity: "))
        cart[item] = qty # Add the item into the Basket
    except ValueError:
        print("Enter a valid integer value")
    #print(cart) # For testing purposes

def updateItem():
    item = input("Enter the item:").title()
    if item in cart:
        print("The item already exists, do you want to update?")
        update_item = input("Enter Y/N: ")
        if update_item.title() == "Y":
            try:
                qty = int(input("Enter the quantity: "))
                cart[item] += qty # Updating an existing item
            except ValueError:
                print("Enter a valid integer number. Please try again!")
        else:
            print("You do not want to update an item in the cart.")
    else:
        print("The item does not exist in the cart. Choose an option.")

def removeItem():
    print("Do you want to remove an item from the cart?")
    remove = input("Enter Y/N: ")
    if remove.title() == "Y":
        item = input("Enter the item: ").title()
        if item in cart:
            del(cart[item])
        else:
            print("Enter a valid item.")
    else:
        print("You do not want to remove an item. Program closed!")

def viewCart():
    for item in cart:
        print(item.title(), ":", cart[item])

def exitCart():
    print("The cart program closed!")


print("Choose one of the following options:\n\n 1. Add Item. \n 2. Update Item. \n 3. Remove Item. \n 4. View Cart. \n 5. Exit Cart.")
print(selectOption())