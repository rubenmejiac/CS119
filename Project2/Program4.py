'''
CS 119
Programmer: Ruben Antonio Mejia Corleto
Date: 03/13/2021
Description: This program combines programs 1 through 3 into one vending machine user interface program. 
             First it welcomes the user and display the drink options, prompt the user for their drink selection, 
             enter their selection, and records the amount due for a small (program 3).
             Next, it displays the size options, prompts the user for the size, enter their size selection,
             and records the price multiplier (program 2). 
             Based on the size entered, the program adjusts the amount due. 
             Next, it displays the amount due, prompt the user for their payment, enter their payment, 
             and determine the amount of change to return (program 1).'''

from decimal import Decimal

# Program 3 functionality
# -----------------------

# Definition of base price for each type of drink
smallPrice1 = 1.70
smallPrice2 = 1.50
smallPrice3 = 1.75
smallPrice4 = 1.80
smallPrice5 = 1.80
smallPrice6 = 1.60
smallPrice7 = 1.65

# Display the menu and ask for input of selection, validating input
print("Welcome to the Coffee Vending Machine")
print("-------------------------------------")
print("Menu:")
print()
print("1.Espresso     (Small $1.70 , Medium $3.40, Large $5.10)")
print("2.Americano    (Small $1.50 , Medium $3.00, Large $4.50)")
print("3.Café au Lait (Small $1.75 , Medium $3.50, Large $5.25)")
print("4.Latte        (Small $1.80 , Medium $3.60, Large $5.40)")
print("5.Cappuccino   (Small $1.80 , Medium $3.60, Large $5.40)")
print("6.Macchiato    (Small $1.60 , Medium $3.20, Large $4.80)")
print("7.Mocha        (Small $1.65 , Medium $3.30, Large $4.95)")
print()
numChoice = int(input("Make your selection by typing the number of your choice: "))
if numChoice < 1 or numChoice > 7:
    print("Invalid option, exiting.")
    quit()
#Depending on selection, assigns the type of coffee selected, 
#gathers the set price for the small size and stores it in a variable amountDue
else:
    if numChoice == 1:
        typeSelected = "Espresso"
        amountDue = smallPrice1
    elif numChoice == 2:
        typeSelected = "Americano"
        amountDue = smallPrice2
    elif numChoice == 3:
        typeSelected = "Café au Lait"
        amountDue = smallPrice3
    elif numChoice == 4:
        typeSelected = "Latte"
        amountDue = smallPrice4
    elif numChoice == 5:
        typeSelected = "Cappuccino"
        amountDue = smallPrice5
    elif numChoice == 6:
        typeSelected = "Macchiato"
        amountDue = smallPrice6
    elif numChoice == 7:
        typeSelected = "Mocha"
        amountDue = smallPrice7
#Displays the type selected and amount due for small size
print ("You selected " + typeSelected + ".")
#print ("The amount due for small size is: $ " + str(amountDue))   #eliminate, unnecesary for user

# Program 2 functionality
# -----------------------

#Asks user for input for size of drink
print()
drinkSizeLetter = input("Choose your coffee size (S)mall (9oz), (M)edium (12oz) or (L)arge (15oz): ")

#Validates input, sets the size chosen, assigns a price multiplier and displays size and multiplier.
if drinkSizeLetter == "S" or drinkSizeLetter == 's':
    drinkSize = "small"
    priceMultiplier = 1
elif drinkSizeLetter == "M" or drinkSizeLetter == "m":
    drinkSize = "medium"
    priceMultiplier = 2
elif drinkSizeLetter == "L" or drinkSizeLetter == "l":
    drinkSize = "large"
    priceMultiplier = 3
else:
    print ("Error: Invalid drink size")
    quit()

# Definition of final drink prices based selected drink base price and multiplier
finalPrice = Decimal(amountDue * priceMultiplier)

print ("You have ordered a " + drinkSize + " drink.")
#print ("The price multiplier is " + str(priceMultiplier))      #eliminate, unnecesary for user


# Program 1 functionality
# -----------------------

# set the item price, display it and ask the user for the payment amount
priceItem = float(finalPrice)  # set value of item
print()
print("Amount due for your drink is: $ " + str(round(finalPrice,2)))
print()
payAmount = float(input("Enter the amount for payment: $ "))

# evaluate the collected amount and determine the correct action to take
if payAmount < priceItem:
    print ("Insufficient funds, no sale.")
    quit()
elif payAmount > priceItem:
    change = Decimal(payAmount - priceItem) # amount of change converted to decimal
    changeDue = round(change,2)             # change rounded to two decimals
    print ("Change: $ " + str(changeDue))

elif payAmount == priceItem:
    print("Exact amount paid.")
print()
print ("Thank you – enjoy your coffee!")
