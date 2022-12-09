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

treeCount = 0
x = 0

for y in range(1, len(lines)):
    x = (x+3) % len(lines[y])

    if lines[y][x] == '#':
        treeCount += 1

print(f"Tree count is {treeCount}")