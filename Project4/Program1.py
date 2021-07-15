'''
CS 119
Programmer: Ruben Antonio Mejia Corleto
Date: 04/10/2021
Project 4 - Program 1
Description: Creates a menu to allow the user to add, insert, remove, find the maximum, 
             the minimum, and sort the list in descending order. 
             Declare your list as list of string.
                    e.g.: studentFullName=["Mike navarro","Miguel saba","Maria Rami"]
             It uses any of the built-in functions. 
             Sample of the output:
                    1- Add an item to the list
                    2- Remove an item from the list
                    3- Insert an item to the list
                    4- Find maximum
                    5- Find Minimum
                    6- Sort the list in descending order
                    7- Quit the program
             Once the user enters an option, the program should execute the code for that
             option and display the list before and after the operations. 
             The program uses a while loop so the program runs until the user enters
             the quit option.
'''
#Declaration of list as a sting list
studentFullNameList = ["Maria Chavez","Gabriela Ford","Ruben Mejia","Thomas Wilcock"]

while True:
    #User input
    print()
    print("    1) Add an item to the list")
    print("    2) Remove an item from the list")
    print("    3) Insert an item to the list")
    print("    4) Find maximum")
    print("    5) Find minimum")
    print("    6) Sort the list in descending order")
    print("    7) Quit the program")
    print()
    
    menuChoice = input("    Please make a choice from the desired menu number: ")
    print()
    #Input validation
    try:
        menuChoice = int(menuChoice)
    except:
        print("     Please use only numeric digits, 1 to 7.")
        continue
    if (menuChoice < 1) or (menuChoice >= 8):
        print ("    Invalid menu option, choose 1 to 7.")
        continue
    #Code execution for each menu option
    #Add an item to the list
    if menuChoice == 1:
        choiceAdd = input("Name that you want to add: ")
        print("Your original list: ", studentFullNameList)
        studentFullNameList.append(choiceAdd)
        print("After adding new name: ", studentFullNameList)
        print("Now the list has " + str(len(studentFullNameList)) + " elements.")
        continue
    #Delete an item from the list by name
    elif menuChoice == 2:
        while True:
            try:
                choiceRemove = input("Name of the student you want to delete: ")
                print("Your original list: ", studentFullNameList)
                studentFullNameList.remove(choiceRemove)
            except:
                print("     Please input complete correct name.")
                continue
            print("After deleting input name: ", studentFullNameList)
            print("Now the list has " + str(len(studentFullNameList)) + " elements.")
            break
        continue
    #Delete an item from the list by index
    elif menuChoice == 3:
        while True:
            try:
                choiceInsertIndex = int(input("Enter the index number in which position do you want to insert the item: "))
                nameToInsertAtIndex = input("Enter the name you want to insert at the chosen position: ")
                studentFullNameList.insert(choiceInsertIndex, nameToInsertAtIndex)
            except:
                print (choiceInsertIndex)
                print("Insert a valid index number.")
                continue
            if (choiceInsertIndex < 0) or (choiceInsertIndex > len(studentFullNameList)):
                print ("    Index does not exist.")
                continue
            print("After inserting new name at index ", choiceInsertIndex, ": ", studentFullNameList)
            print("Now the list has " + str(len(studentFullNameList)) + " elements.")
            break
        continue
    #Find and display the maximum element
    elif menuChoice == 4:
        while True:
            maxElement = max(studentFullNameList)
            print ("The maximum is: ", maxElement)
            break
        continue
    #Find and display the minimum element
    elif menuChoice == 5:
        while True:
            minElement = min(studentFullNameList)
            print ("The minimum is: ", minElement)
            break
        continue
    elif menuChoice == 6:
        studentFullNameList.sort(reverse = True)
        print ("List sorted in descending order is: ", studentFullNameList)
        continue
    elif menuChoice == 7:
        print("Exiting program.")
        print()
        studentFullNameList = ""
        exit()
    break



