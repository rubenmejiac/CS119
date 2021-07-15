'''
CS 119
Programmer: Ruben Antonio Mejia Corleto
Date: 05/07/2021
Project 5 - Program 1
Requirements: ----- Lists and functions -----
             For this program, you have to write your own functions without using any of the built-in functions.  
                List functions that CAN'T be used: insert(), append(), remove(), del(), max(), min(), reverse(), sort(), etc.
                Only functions that you MAY use:   len(), index(). 
             These are your lists:
                employees=["Mike navarro","Miguel saba","Maria Rami"]
                salaries=  [20000.00, 30000.00, 40000.00]
             Create the following menu: 
                1- Add a new Employee 
                2- Remove an Employee
                3- Insert new Employee 
                4- Sort salaries in descending order
                5- Search for an employee 
                6- find total salary
                7- Display the list of employees
                8- Quit the program .....exit()
              Here is more details for every function:
                1- Add a new Employee ..........addEmployee(employee, salary)  
                2- Remove an Employee .......removeEmployee(employee, salary)
                3- Insert an Employee into a specific location.....insertNewEmployee(employee, index, salary)
                4- Sort salaries in descending order .....sortSalaries(employees, salaries)
                5- Search function for an employee ....searchEmployee(employee) --> will return the index and the salary
                6- find total salary ... totalSalary(salaries )  
                7- Display the list.... displayList(employees,  salaries)
                8- Quit the program .....exit()
              Here is a sample output:
                Please enter your option: 3 
                Where do you want to insert the item? (Enter the index number) 1
                Please enter the employee name you want to insert: "Tina Mari"
                Please enter the employee salary you want to insert: 65000.00
               Your program should call the function insertNewEmployee(employee, index, salary)
               Your List before:
                employees = ["Mike navarro","Miguel saba","Maria Rami"]
                salaries=  [20000.00, 30000.00, 40000.00]
               After inserting an item into index 1:
                employees = ["Mike navarro","Tina Mari", "Miguel saba","Maria Rami"]
                salaries=  [20000.00, 65000.00, 30000.00, 40000.00]
              Once the user enters an option, your program should execute the code for that option and displays 
              the list before and after the operations. 
              Make sure to use a while loop so the program runs until user enters the quit option.
'''
employees = ["Mike Navarro","Miguel Ssaba","Maria Rami"]
salaries = [20000.00, 30000.00, 40000.00]

def addEmployee(employee, salary):
    global employees
    global salaries
    employees += [employee]
    salaries += [salary]

def displayList(employees, salaries):
    print ("  Employees: ", employees)
    print ("  Salaries:  ", salaries)

def removeEmployee(employee, salary):
    global employees
    global salaries
    indexEmployeeToRemove = employees.index(employee)
    indexSalaryToRemove = salaries.index(salary)
    employees = employees[:indexEmployeeToRemove] + employees[indexEmployeeToRemove+1:]
    salaries = salaries[:indexSalaryToRemove] + salaries[indexSalaryToRemove+1:]

def insertNewEmployee(employee, position, salary):
    global employees
    global salaries
    i = employees[:]
    i[position:position] = [employee]
    employees = [i]
    s = salaries[:]
    s[position:position] = [salary]
    salaries = [s]

def sortSalaries():
    global employees
    global salaries
    newSalaries = []
    while salaries:
        maxSalary = salaries[0]
        for x in salaries:
            if x > maxSalary:
                maxSalary = x
        newSalaries.append(maxSalary)
        salaries.remove(maxSalary)
    salaries = newSalaries

def searchEmployee(employee):
    global employees
    global salaries
    global foundAt 
    foundAt = employees.index(employee)
    salaries = salaries[:foundAt]

def totalSalary(salary):
    global salaries
    total = 0
    for x in salary:
        total += x
    salaries = total

option = 0      
while option != 8:

    option = int(input("1 - Add a new Employee\n2 - Remove an Employee\n3 - Insert new Employee\n4 - Sort salaries in descending order\n5 - Search for an Employee\n6 - Find total salary\n7 - Display the list of Employees\n8 - Quit the program\nPlease select one of the options: "))

    if option == 1:
        print("Your list before: ")
        displayList(employees, salaries)
        employee = input("Please enter the employee name to add: ")
        salary = float(input("Please enter the salary for the employee: $"))
        addEmployee(employee, salary)
        print("Your list after adding employee: ")
        displayList(employees, salaries)

    elif option == 2:
        print("Your list before: ")
        displayList(employees, salaries)
        employee = input("Please enter the employee name you want to remove: ")
        salary = float(input("Please enter the salary for the employee: $"))
        removeEmployee(employee, salary)
        print("Your list after removing employee: ")
        displayList(employees, salaries)

    elif option == 3:
        print("Your list before: ")
        displayList(employees, salaries)
        employee = input("Please enter the employee name you want to insert: ")
        position = int(input("Please enter the position for insertion: "))
        salary = float(input("Please enter the salary for the new employee: $"))
        insertNewEmployee(employee, position, salary)
        print("Your list after inserting new employee at desired position: ")
        displayList(employees, salaries)

    elif option == 4:
        print("Your list before: ")
        displayList(employees, salaries)
        sortSalaries()
        print("Your sorted list of salaries in descending order: ")
        print (salaries)

    elif option == 5:
        print("Your list before: ")
        displayList(employees, salaries)
        employee = input("Please enter the employee name you want to search: ")
        searchEmployee(employee)
        print("Employee found at index: " + str(foundAt))
        print("Employee salary is: $" + str(salary))
    
    elif option == 6:
        print("Your list: ")
        displayList(employees, salaries)
        totalSalary(salaries)
        print("Employee total salary is: $" + str(salaries))
    

    elif option == 7:
        displayList(employees, salaries)

exit()