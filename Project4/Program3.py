'''
CS 119
Programmer: Ruben Antonio Mejia Corleto
Date: 04/09/2021
Project 4 - Program 3
Description: 
did not do the exercise
'''

#User input
accountNumber = int(input("Enter your account number: "))
serviceCode = str(input("Service code: "))
if len(serviceCode) > 1:                #validate service code lenght and value
    print ("Invalid service code")
    quit()
elif (serviceCode == "r") or (serviceCode == "R") :
    minutes = int(input("Number of minutes service was used: "))
elif (serviceCode == "p") or (serviceCode == "P") :
    minutesDay = int(input("Number of minutes service was used between 6:00am and 6:00pm: "))
    minutesNight = int(input("Number of minutes service was used between 6:00pm and 6:00am: ")) 

#Calculation of bill
amountDue = 0

#could not finish, I did not calculate time correctly.
