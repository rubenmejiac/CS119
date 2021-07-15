'''
---------------------------------------
CS 119
Programmer: Ruben Antonio Mejia Corleto
Date: 05/31/2021
Final Project
----------------------------------------
You are going to write a program called BankApp to simulate a banking application.
The information needed for this project are stored in a text file. Those are:
usernames, passwords, and balances.
Your program should read username, passwords, and balances for each customer, and
store them into three lists: userName (string), passWord(string), balances(float)
The .txt file with information is provided as UserInformation.txt

Example: This will demonstrate if file only contains information of 3 customers. You
could add more users into the file.
userName passWord Balance
-------------------------
Mike sorat1237# 350
Jane para432@4 400
Steve asora8731% 500

When a user runs your program, it should ask for the username and password
first. Check if the user matches a customer in the bank with the information
provided. Remember username and password should be case sensitive.
After asking for the user name, and password display a menu with the following
options and ask the user for input (Use a While Loop).

Type D to deposit money
    If the user types D (Deposit Function) Ask the user to enter the amount to 
    deposit. Then call the Deposit Function, passing the deposit amount as a 
    parameter. The function should update the Balance. 
    Then display the new balance (this should happen by calling the ShowBalance
    function). Then display the menu again
Type W to withdraw money 
    If the user types W (Withdraw Function) Ask the user to enter the amount 
    he/she wants to withdraw. Before calling the withdraw function, make sure 
    there is enough balance. Call the ShowBalance function before Withdraw function!! 
    Then call the Withdraw Function, passing the withdraw amount as a parameter. 
    The function should update the Balance. Display the new balance to the user. 
    Then display the menu again
Type B to display Balance 
    If the user enters B (ShowBalance Function) Display the Balance. 
Type C to change user, display user name 
    If the user enters C (ChangeUser Function) Ask for the user name and change to a
    different customer.
Type A to add new client
    If the user enters A (AddNewUser function) Ask for username, password, and 
    balance. These information will be added to the appropriate lists which 
    later on will be transfered to the UserInformation.txt
    If the user types any other option: Prompt the user that option is invalid
Type E to exit 
    If the user types E then terminate the program and update the UserInformtion.txt
    with the correct updated balances. 
PS: You program must keep displaying the menu until the user types the option E, 
to exit the program.
'''
import os
import datetime

def deposit(username, balance):
    deposit_amount = float(input('Please enter amount to be deposited:'))
    file = open(filename,'a')
    balance = 0
    new_balance = 0
    with open(filename,'r') as file:
        for i in file:
            balance = float(i)
    with open(filename,'w+') as file2:
        new_balance = balance + deposit_amount
        new_balance = str(new_balance)
        file2.write(new_balance)
        print('Your new balance is:',new_balance)
    with open (transactionfilename,'a') as file3:
        balance = str(balance)
        deposit_amount = str(deposit_amount)
        file3.write(str(datetime.datetime.now()))
        file3.write('\nPrevious balance: '+balance+'. Deposit amount is:'+deposit_amount+'. New balance:'+new_balance+'\n')
    
    file.close()

def withdrawal():
    withdrawn = float(input('Please enter amount to withdraw:'))
    file = open(filename,'a')
    balance = 0
    new_balance = 0
    with open(filename,'r') as file:
        for i in file:
            balance = float(i)
    with open(filename,'w+') as file2:
        if withdrawn > balance:
            print('Insufficient balance. Your balance is:',balance)
        else:
            new_balance =  balance - withdrawn
            new_balance = str(new_balance)
            file2.write(new_balance)
            print('New balance is:',new_balance)
            with open (filename,'a') as file2:
                balance = str(balance)
                withdrawn = str(withdrawn)
                file2.write(str(datetime.datetime.now()))
                file2.write('\nPrevious balance: '+balance+'. Withdrawn amount is:'+withdrawn+'. New balance:'+new_balance+'\n')
    file.close()

def balance(userName):
    global username
    balances = float(i)
    file.seek(0)
    if file.read(1):
        print ('Balance is:', balance)
    else:
        print('No balance left')  
    file.close()

def addUser():
    global username, password
   
print('Banking Application')
print('Please login to proceed.')

#Create and populate three arrays with 3 columns information from text file
userName = []
passWord = []
balances = []
with open('UserInformation.txt') as textFile:
    for line in textFile:
        row = line.split()
        userName.append(row[0])
        passWord.append(row[1])
        balances.append(float(row[-1]))

#Login, validate user and password
username = input('Enter your username: ')
password = input('Enter your password: ')
if username in userName and password in passWord:
    print('Login successful')
    
#Display menu    
    while True:
        print('\nType D to Deposit Money\nType W to Withdraw Money\nType B to Display Balance\nType C to Change User, Display Username\nType A to Add New Client\nType E Exit')
        opt = input('Enter your choice:')
        if(opt == "D"):
            deposit()
            break
        elif(opt == "W"):
                withdrawal()
                break
        elif(opt == "B"):
                balance()
                break
        elif(opt == "C"):
            transactionfilename = username+'_transactionhistory.txt'
            transactionfile = open(transactionfilename,'a')
            with open (transactionfilename,'r') as f:
                f.seek(0)
                if f.read(1):
                    print(f.read())
                    break
                else:
                    print('There is no transaction history.')
                    break
        elif(opt == "A"):
                addUser()
                break
        elif (opt == "E"):
            print('Exiting program.')
            break
        else:
            print('You typed an invalid option')
            opt= input('Do you want to continue? Type Y to Continue, N to Terminate:')
        
else:
    print('Incorrect username or password, please try again')