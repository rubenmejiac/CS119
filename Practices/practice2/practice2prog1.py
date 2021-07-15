'''
Programmer Name: Ruben Antonio Mejia Corleto
Date: 02/15/2020
Description: program that asks the user to enter a number. 
             Write some conditional statement to check whether the number entered by the user is even or odd.
'''

num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("The number is even.")
else:
    print("The number is odd.")
