'''
CS 119
Programmer: Ruben Antonio Mejia Corleto
Date: 03/27/2021
Description: Program to calculate the average score and letter grade for students in CS119.
             Ask how many students the Professor has in his CS119
             The program loops asking for the following data:
                - Ask the student name
                - Ask for 3 exam scores
             Calculates the average score.
             Using a bunch of IF conditions, the computer should determine the grade 
             and display it to the user, using the following criteria:
                 - If Average is 98-100 assign the grade “A+”
                 - If Average is 95-98 assign the grade “A”
                 - If Average is 91-95 assign the grade “A-”
                 - If Average is 88-91 assign the grade “B+”
                 - If Average is 84-88 assign the grade “B”
                 - If Average is 80-84 assign the grade “B-”
                 - If Average is 75-80 assign the grade “C+”
                 - If Average is 70-75 assign the grade “C”
                 - If Average is less than 70 and greater than 60 assign the grade “D”
                 - If Average is less than or equal 60 assign grade "NC"
             Display the student name and the grade back to the user.
'''
from decimal import Decimal

for student in range (1, 4):
    accumScore = 0
    studentName = input("\nPlease enter your name: ")  # asks for student name
    if studentName is None:
        print("Exiting, name cannot be blank")
        exit()
    for examScore in range (1, 4):                      # loops imput for 3 exam scores
        score = int(input(" Score " + str(examScore) + ": "))
        accumScore += score                             #
        averageScore = accumScore / 3
    if averageScore >= 98 and averageScore <= 100:
        grade = "A+"
    elif averageScore >= 95 and averageScore < 98:
        grade = "A"
    elif averageScore >= 91 and averageScore < 95:
        grade = "A-"
    elif averageScore >= 88 and averageScore < 91:
        grade = "B+"
    elif averageScore >= 84 and averageScore < 88:
        grade = "B"
    elif averageScore >= 80 and averageScore < 84:
        grade = "B-"
    elif averageScore >= 75 and averageScore < 80:
        grade = "C+"
    elif averageScore >= 70 and averageScore < 75:
        grade = "C"
    elif averageScore > 60 and averageScore < 70:
        grade = "D"
    else : 
        grade = "NC"
    Score = round(averageScore, 2)    
    print(studentName + " grade is: " + grade + " (" + str(Score) + ")")
    
        
    