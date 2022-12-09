data = []
with open("cal_data.txt") as file:
    data = file.read()
    contents = data.split("\n\n")   # split data into list of strings by finding every blank line (two newlines in a row)

# convert each string into a list of strings and append to a new list
sl = []
for i in range(0, len(contents)):
    sl.append(contents[i].split("\n"))

# convert each list of strings into one int (sum) and append to new list
calories = []

for elf in sl:
    cals = 0
    for food in elf:
        cals += int(food)
    calories.append(cals)

# sort the list of total calories 
calories.sort()

# find the three largest values (the last three in the list) and add them together
max = 0
for i in range(3):
    max += calories.pop()

print(max)
