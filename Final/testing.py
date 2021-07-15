userName = []
passWord = []
balances = []
with open('UserInformation.txt') as textFile:
    for line in textFile:
        row = line.split()
        userName.append(row[0])
        passWord.append(row[1])
        balances.append(float(row[-1]))

print (userName)
print (passWord)
print (balances)