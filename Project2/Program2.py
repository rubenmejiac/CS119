'''
CS 119
Programmer: Ruben Antonio Mejia Corleto
Date: 03/11/2021
Description: A program to determine the drink size and price multiplier based on the letter the user enters
             in the Coffee Vending Machine.
             The machine provides coffee in three sizes: small (9oz), medium (12oz), and large (15oz).
             The program prints a message to the user giving the various drink size options and then prompts the user
             for the drink size. 
             The user can enter an ‘s’ or‘S’ for small, an ‘m’ or ‘M’ for medium, and an ‘l’ or ‘L’ for large. 
             Depending on which size the user requests, it prints a message such as: 
             “You have ordered a (small, medium, large) drink.” 
             In addition to displaying the size ordered, it also record a price multiplier. 
             The price multiplier for a small is 1, for a medium is 2, and for a large is 3. 
             If the user does not enter a valid character, print an error message (such as “Error: Invalid drink size”)
             and exit the program. 
             The program uses if-then-else statements for this problem.
             After the if-then-else statements, it prints the value of the price multiplier to ensure that the correct
             value was recorded. 
'''

#Asks user for input for size of drink
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
print ("You have ordered a " + drinkSize + " drink.")
print ("The price multiplier is " + str(priceMultiplier))
