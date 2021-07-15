'''
Programmer Name: Ruben Antonio Mejia Corleto
Date: 02/15/2020
Description: a program that allows the user to enter values for a salesperson’s base salary, total sales, and commission rate. The program computes and outputs the salesperson’s pay by adding the base salary to the product of the total sales and commission rate
'''

base_sal = int(input("Base salary: "))
tot_sales = float(input("Total sales: "))
com_rate = float(input("Commission rate (in percentage): "))
pay = base_sal + (tot_sales * (com_rate / 100))
print("The salesperson's pay is $" + str(round(pay,2)))