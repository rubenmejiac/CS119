'''
CS 119
Programmer: Ruben Antonio Mejia Corleto
Date: 03/11/2021
Description: Money collection interface for the coffee vending machine.
             This program tells the user the price of the item and then the user will enter the amount
             of money they are paying (this simulates them actually inserting cash). 
             -If the money collected is less than the price, it prints an appropriate message
              (such as: “Insufficient funds, no sale!”) and then the program exits.
             -If enough money is collected, the program determines the amount to return to the customer.   
             -If the change due is not zero, it tells the user how much change they will receive. 
             Next, it print a message (such as “Thank you – enjoy your coffee!”) and the program ends normally.

             Note: the program should be able to handle all amounts of money (not just multiples of dollars
             but also cents such as $1.25). 
             Also it may assume that the user is only entering a number and not the $ (though the $ could be
             part of your prompt).
             Hint: Check how to do floating point comparisons
'''

from decimal import Decimal
print ("Welcome to the Coffee Vending Machine")

# set the item price, display it and ask the user for the payment amount
priceItem = float(3.55) # set value of item
print ("Price of the item is: $ " + str(priceItem))
payAmount = float(input("Enter the amount for payment:  $ "))

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

print ("Thank you – enjoy your coffee!")
