'''
CS 119
Programmer: Ruben Antonio Mejia Corleto
Date: 03/12/2021
Description: This program displays the various coffee drinks your vending machine offers along with the option number
             for each drink. For each option it includes the price 
             The cost for the small is pre-set, the costs for medium is 2 times the cost of the small
             and the cost of the large is 3 times the cost of the small.
             The program prompts the user for their drink selection.
             It then records the cost of the small drink into a variable that will be used to compute the amount due. 
             It displays a message i.e. “You selected Americano”. 
             If the user does not enter a valid option, it prints an error message and the program terminates. 
             A conditional statement is used for this problem. 
             After the statement, the program displays the amount due for the small size of the drink selected.
'''

# Definition of base price for each type of drink
smallPrice1 = 1.70
smallPrice2 = 1.50
smallPrice3 = 1.75
smallPrice4 = 1.80
smallPrice5 = 1.80
smallPrice6 = 1.60
smallPrice7 = 1.65

# Definition of medium and large prices for each type of drink
medPrice1 = smallPrice1 * 2
medPrice2 = smallPrice2 * 2
medPrice3 = smallPrice3 * 2
medPrice4 = smallPrice4 * 2
medPrice5 = smallPrice5 * 2
medPrice6 = smallPrice6 * 2
medPrice7 = smallPrice7 * 2
largePrice1 = smallPrice1 * 3
largePrice2 = smallPrice2 * 3
largePrice3 = smallPrice3 * 3
largePrice4 = smallPrice4 * 3
largePrice5 = smallPrice5 * 3
largePrice6 = smallPrice6 * 3
largePrice7 = smallPrice7 * 3

# Display the menu and ask for input of selection, validating input
print("Welcome to the Coffee Vending Machine")
print("-------------------------------------")
print()
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
numChoice = int(input("Please make your selection by typing the number of your choice: "))
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
print ("The amount due for small size is: $ " + str(amountDue))
