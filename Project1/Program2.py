'''
Programmer: Ruben Antonio Mejia Corleto
Date: 02/25/2020
Description: A program that asks for the yearly salary of five people (one at a time).
             Using the Accumulation concept, it calculates and displays the total salary
             from all five people combined.
'''

# Variable inizialization
accum = 0

# Input the yearly salary of 5 people
sal1 = int(input("Yearly salary for person 1: $ "))
accum = accum + sal1
sal2 = int(input("Yearly salary for person 2: $ "))
accum = accum + sal2
sal3 = int(input("Yearly salary for person 3: $ "))
accum = accum + sal3
sal4 = int(input("Yearly salary for person 4: $ "))
accum = accum + sal4
sal5 = int(input("Yearly salary for person 5: $ "))
accum = accum + sal5

# Output: display total salary of 5 people
print ("\nThe total salary is: $ " + str(accum))

''' output:
Yearly salary for person 1: $ 50000
Yearly salary for person 2: $ 29300
Yearly salary for person 3: $ 22000
Yearly salary for person 4: $ 33600
Yearly salary for person 5: $ 44000

The total salary is: $ 178900


'''