'''
CS 119
Programmer: Ruben Antonio Mejia Corleto
Date: 03/27/2021
Description: Using For... loop, this program asks for the name, salary and the state
             for 6 employees.
             It calculates the federal tax, state tax and the net salary for
             each employee, using the following criteria:

             To calculate the federal tax, it uses the following criteria:
             If the salary is greater than 100,000 then it calculates the federal
             tax at 20 percent.
             Otherwise it calculates the federal tax at 15%.

             To calculate the state Tax, it uses the following criteria:
             If the employee is from CA, NV, AZ, or TX calculate the state tax at 10%
             Otherwise it calculates the state tax at 12%

             The program then calculates and display the net salary of the employee.
             To calculate the net salary, it subtracts the federal and state tax
             from the gross salary.
'''

from decimal import Decimal

for employee in range (1, 7):
    # Collect the information from each employee
    userName = input("Employee " + str(employee) + ", please enter your name: ")
    if userName is None:                     #validate user name
        print("Exiting, name cannot be blank")
        exit()
    salary = float(input("Salary: $"))
    if salary is None:
        print("Exiting, salary has to have a value")
        exit()
    elif salary <= 0:                       #validate salary 0 or negative
        print("Exiting, salary has to be positive and greater than 0")
        exit()
    state = input("State: ")
    if state is None:                       #validate state is not empty
        print("Exiting, state has to have a value")
        exit()
    #validate state 2 letter abbreviations
    elif (state == "AL") or (state == "AK") or (state == "AZ") or (state == "AR") \
    or (state == "CA") or (state == "CO") or (state == "CT") or (state == "DE") \
    or (state == "DC") or (state == "FL") or (state == "GA") or (state == "HI") \
    or (state == "ID") or (state == "IL") or (state == "IN") or (state == "IA") \
    or (state == "KS") or (state == "KY") or (state == "ME") or (state == "MD") \
    or (state == "MA") or (state == "MI") or (state == "MN") or (state == "MS") \
    or (state == "MO") or (state == "MT") or (state == "NE") or (state == "NV") \
    or (state == "NJ") or (state == "NM") or (state == "NY") or (state == "NC") \
    or (state == "ND") or (state == "OH") or (state == "OK") or (state == "OR") \
    or (state == "PA") or (state == "RI") or (state == "SC") or (state == "SD") \
    or (state == "NJ") or (state == "NM") or (state == "NY") or (state == "NC") \
    or (state == "VA") or (state == "WA") or (state == "WV") or (state == "WI") \
    or (state == "WY") \
    or (state == "al") or (state == "ak") or (state == "az") or (state == "ar") \
    or (state == "ca") or (state == "co") or (state == "ct") or (state == "de") \
    or (state == "dc") or (state == "fl") or (state == "ga") or (state == "hi") \
    or (state == "id") or (state == "il") or (state == "in") or (state == "ia") \
    or (state == "ks") or (state == "ky") or (state == "me") or (state == "md") \
    or (state == "ma") or (state == "mi") or (state == "mn") or (state == "ms") \
    or (state == "mo") or (state == "mt") or (state == "ne") or (state == "nv") \
    or (state == "nj") or (state == "nm") or (state == "ny") or (state == "nc") \
    or (state == "nd") or (state == "oh") or (state == "ok") or (state == "or") \
    or (state == "pa") or (state == "ri") or (state == "sc") or (state == "sd") \
    or (state == "nj") or (state == "nm") or (state == "ny") or (state == "nc") \
    or (state == "va") or (state == "wa") or (state == "wv") or (state == "wi") \
    or (state == "wy") :
        # Calculate federal tax
        if salary > 100000:
            taxPercent = 0.2
        else :
            taxPercent = 0.15
        federalTax = salary * taxPercent
    
        # Calculate state tax
        if (state == "CA") or (state =="NV") or (state == "AZ") or (state == "TX") \
        or (state == "ca") or (state =="nv") or (state == "az") or (state == "tx"):
            stateTaxPercent = 0.1
        else :
            stateTaxPercent = 0.12
        stateTax = salary * stateTaxPercent
    
        # Calculate and display net salary
        netSalary = Decimal(salary - federalTax - stateTax)
        result = round(netSalary,2)
        print (userName + " (employee " + str(employee) + ") Net Salary is: $" + str(result))
    else:
        print (state)
        print("Exiting, state has to have a valid US two letter identifier")
        exit()    
    
