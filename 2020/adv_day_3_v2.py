import os

# my_file = open("trees.txt", "r")
# slopes = my_file.readlines()

# slopes = [x.strip() for x in slopes]

# # newSlopes = []

# # for row in slopes:
# #     for i in range(5):
# #         row = row + row
# #     newSlopes.append(row)

# numTrees = 0

# pos = 3

# # print(newSlopes)

# for i in range(1, len(slopes)-1):
#     # if slopes[i][pos] == "#":
#     #     numTrees += 1
#     print(slopes[i][pos])
#     pos += 3
#     if pos >= len(slopes[0]):
#         pos = pos - len(slopes[0])

# print(numTrees)

with open('trees.txt') as f:
    lines = f.read().splitlines()

tempTotal = 1
total = 1
x = 0
treeCount = 0

i = 1
for y in range(1, len(lines), 2):
    
    x = (x+1) % len(lines[i])

    if lines[y][x] == '#':
        treeCount += 1
    i += 1

tempTotal = tempTotal * treeCount
print(f"temp count is {tempTotal}")

slopes = [1, 3, 5, 7]
for slope in range(1, len(slopes)):
    treeCount = 0
    for y in range(1, len(lines)):
        x = (x+slopes[slope]) % len(lines[y])

        if lines[y][x] == '#':
            treeCount += 1
    total = total * treeCount
    print(f"total for slope {slopes[slope]} is {total}")

total = total * tempTotal


print(total)