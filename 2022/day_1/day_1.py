data = []
with open("cal_data.txt") as file:
    data = file.read()
    contents = data.split("\n\n")


sl = []
for i in range(0, len(contents)):
    sl.append(contents[i].split("\n"))

calories = []

for elf in sl:
    cals = 0
    for food in elf:
        cals += int(food)
    calories.append(cals)


calories.sort()
max = calories.pop()
# for i in range(3):
#     max += calories.pop()

print(max)
# print(max, max_1, max_2)
# print(max + max_1 + max_2)