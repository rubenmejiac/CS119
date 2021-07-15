'''
Programmer Name: Ruben Antonio Mejia Corleto
Date: 02/15/2020
Description: program that asks for the names of three runners and the time it took each of them
to ﬁnish a race. The program should display who came in ﬁrst, second, and third place.
Think about how many test cases are needed to verify that your problem works correctly.
'''

runner1_name = input("Runner 1 name: ")
runner1_time = int(input("Runner 1 time (seconds): "))
runner2_name = input("Runner 2 name: ")
runner2_time = int(input("Runner 2 time (seconds): "))
runner3_name = input("Runner 3 name: ")
runner3_time = int(input("Runner 3 time (seconds): "))

if (runner1_time <= runner2_time) and (runner1_time <= runner3_time):
    fastest = runner1_time
    first_place = runner1_name
elif (runner2_time <= runner1_time) and (runner2_time <= runner3_time):
    fastest = runner2_time
    first_place = runner2_name
else:
    fastest = runner3_time
    first_place = runner3_name

if (runner1_time >= runner2_time) and (runner1_time >= runner3_time):
    slowest = runner1_time
    third_place = runner1_name
elif (runner2_time >= runner1_time) and (runner2_time >= runner3_time):
    slowest = runner2_time
    third_place = runner2_name
else:
    slowest = runner3_time
    third_place = runner3_name

if (first_place == runner1_name) and (third_place == runner2_name):
    middle = runner3_time
    second_place = runner3_name
elif (first_place == runner2_name) and (third_place == runner3_name):
    middle = runner1_time
    second_place = runner1_name
else: 
    middle = runner2_time
    second_place = runner2_name
    
print(first_place, "came in first place with", str(fastest), "seconds.")
print(second_place, "came in second place with", str(middle), "seconds.")
print(third_place, "came in third place with", str(slowest), "seconds.")

if (runner1_time == runner2_time) or (runner2_time == runner3_time) or (runner1_time == runner3_time):
    print("There was a tie in one or more finish positions")



