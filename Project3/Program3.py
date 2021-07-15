'''
CS 119
Programmer: Ruben Antonio Mejia Corleto
Date: 03/27/2021
Description: Program that calculates and prints the bill for a cellular telephone company.
             A telephone company offers two types of service: regular and premium. 
             Its rate vary, depending on the type of service. The rates are compared as follows:
             Regular service:    $10.00 plus first 50 minutes are free. 
                                 Charges for over 50 minutes are $0.20 per minute.
             Premium service:   $25 plus:
                                For calls made from 6:00 a.m. to 6:00 p.m., the first 75 minutes are free; 
                                charges for more than 75 minutes are $0.10 per minute
                                For calls made from 6:00 pm to 6:00 a.m., the first 100 minutes are free; 
                                charges for more than 100 minutes are $0.05 per minute.
            The program should prompt the user to enter an account number, a service code (type character), 
            and the number of minutes the service was used. 
            A service code of r or R means regular service; 
            A service code of p or P means premium service. 
            Treats any other character as an error. 
            The program should output the account number, type of service, number of minutes the telephone service was used, 
            and the amount due from the user.
            For the premium service, the customer may be using the service during the day and the night. 
            Therefore, to calculate the bill, you must ask the user to input the number of minutes the service was used 
            during the day and the number of minutes the service was used during the night.
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



    