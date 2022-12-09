import os

my_file = open("pwords.txt", "r")
pwords = my_file.readlines()

pwords = [x.strip() for x in pwords]

passwordsDicts = []
validPasswords = 0

for pword in pwords:   
    newList = pword.split()
    
    newList[1] = newList[1][0:-1]
    minMax = newList[0].split('-')
    minimum = int(minMax[0])
    maximum = int(minMax[1])

    item = {
        'minInstances' : minimum,
        'maxInstances' : maximum,
        'letter' : newList[1],
        'password' : newList[2]
    }

    passwordsDicts.append(item)

for item in passwordsDicts:
    count = item['password'].count(item['letter'])
    # print(item['password'])
    
    
    if item['minInstances'] <= count and count <= item['maxInstances']:
        validPasswords += 1




print(validPasswords)