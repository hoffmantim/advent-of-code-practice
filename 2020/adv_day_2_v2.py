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
    minimum = int(minMax[0]) - 1
    maximum = int(minMax[1]) - 1

    item = {
        'firstPos' : minimum,
        'secondPos' : maximum,
        'letter' : newList[1],
        'password' : newList[2]
    }

    passwordsDicts.append(item)

# print(passwordsDicts)
for item in passwordsDicts:
    # if item['password'][(item['firstPos'])] == item['letter'] and item['password'][(item['secondPos'])] != item['letter']:
    #     validPasswords += 1
    first = item['password'][(item['firstPos'])]
    second = item['password'][(item['secondPos'])]
    letter = item['letter']

    if (first == letter or second == letter) and first != second:
        validPasswords += 1
        


print(validPasswords)