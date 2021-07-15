'''
CS 119
Programmer: Ruben Antonio Mejia Corleto
Date: 04/10/2021
Project 4 - Program 2
Description: Mike, Tina, Jason, Vicky, and Tammy are preparing for an upcoming marathon. 
             Each day of the week, they run a certain number of miles and write them into a notebook. 
             At the end of the week, they would like to know the number of miles run each day, 
             the total miles for the week, and average miles run each day 
             This program helps them analyze their data. 
             The program contain parallel lists: a list to store the the names of the runners 
             and a two-dimensional list of five rows and seven columns to store the number of miles 
             run by each runner each day.  
'''
runners = ["Mike", "Tina", "Jason", "Vicky", "Tammy"]
twoDimensionList = [] 

milesMike = []
milesMike.append(runners[0] + "   ")
for i in range(1, 8):
    daysMike = list(map(float, input("Miles runned by Mike for day " + str(i) + ": ").split()))
    milesMike.append(daysMike) 
avgMikeMiles = sum(daysMike) / len(daysMike)
milesMike.append(avgMikeMiles)      
twoDimensionList.append(milesMike)

milesTina = []
milesTina.append(runners[1] + "   ")
for i in range(1, 8):
    daysTina = list(map(float, input("Miles runned by Tina for day " + str(i) + ": ").split()))
    milesTina.append(daysTina)
avgTinaMiles = sum(daysTina) / len(daysTina)
milesTina.append(avgTinaMiles)      
twoDimensionList.append(milesTina)

milesJason = []
milesJason.append(runners[2] + "  ")
for i in range(1, 8):
    daysJason = list(map(float, input("Miles runned by Jason for day " + str(i) + ": ").split()))
    milesJason.append(daysJason)
avgJasonMiles = sum(daysJason) / len(daysJason)
milesJason.append(avgJasonMiles)      
twoDimensionList.append(milesJason)

milesVicky = []
milesVicky.append(runners[3] + "  ")
for i in range(1, 8):
    daysVicky = list(map(float, input("Miles runned by Vicky for day " + str(i) + ": ").split()))
    milesVicky.append(daysVicky)
avgVickyMiles = sum(daysVicky) / len(daysVicky)
milesVicky.append(avgVickyMiles)      
twoDimensionList.append(milesVicky)

milesTammy = []
milesTammy.append(runners[4] + "  ")
for i in range(1, 8):
    daysTammy = list(map(float, input("Miles runned by Tammy for day " + str(i) + ": ").split()))
    milesTammy.append(daysTammy)
avgTammyMiles = sum(daysTammy) / len(daysTammy)
milesTammy.append(avgTammyMiles)      
twoDimensionList.append(milesTammy)

print("Runner  Day1   Day2   Day3   Day4   Day5   Day6   Day7   Average")
for x in range(len(twoDimensionList)): 
    for y in range(len(twoDimensionList[x])):
        print(twoDimensionList[x][y], end = " ")
    print()

quit()