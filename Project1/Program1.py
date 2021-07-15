'''
Programmer: Ruben Antonio Mejia Corleto
Date: 02/23/2020
Description: Dinner check split.
             Write a program to collect the following data from the 3 users.
            1. Name
            2. Amount of Lunch Menu item
            3. Amount of Drink
 Calculate and output Name and the Amount of each person's check including 15% tip.
'''

# Get input for 3 users' names, amount of food and drinks
user1_name = input("User 1 Name: ")
user1_food = float(input("User 1 food amount: $ "))
user1_drink = float(input("User 1 drink amount: $ "))
user2_name = input("User 2 Name: ")
user2_food = float(input("User 2 food amount: $ "))
user2_drink = float(input("User 2 drink amount: $ "))
user3_name = input("User 3 Name: ")
user3_food = float(input("User 3 food amount: $ "))
user3_drink = float(input("User 3 drink amount: $ "))

# set the tip percentage
tip_percentage = 0.15

# calculate value of food and drinks
user1_total = user1_food + user1_drink + ((user1_food + user1_drink) * 0.15)
user2_total = user2_food + user2_drink + ((user2_food + user2_drink) * 0.15)
user3_total = user3_food + user3_drink + ((user3_food + user1_drink) * 0.15)

total = user1_total + user2_total + user3_total

# output the results to screen as indicated
print(user1_name + " $ " + str(round(user1_total,2)))
print(user2_name + " $ " + str(round(user2_total,2)))
print(user3_name + " $ " + str(round(user3_total,2)))

''' Output
Sara $ 43.12
Ruben $ 39.66
David $ 33.09
'''
