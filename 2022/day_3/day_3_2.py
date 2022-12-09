priority = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("bags.txt") as f:
    data = f.read()
    contents = data.split("\n")


groups = []
total = 0

while len(contents) > 0:
    group = []
    for i in range(3):
        group.append(contents.pop())
    groups.append(group)

badges = []
for group in groups:
    for i in range(0, len(group[0])):
        if group[0][i] in group[1] and group[0][i] in group[2]:
            badges.append(group[0][i])
            break

print(total)
print(len(badges))
for badge in badges:
    val = priority.index(badge)
    total += val

print(total)

# for item in contents:
#     middle = (len(item)//2)
#     left = item[:middle]
#     right = item[middle:]
#     rucksacks.append([left, right])

# items = []

# for sack in rucksacks:
#     val = 0
#     for i in range(0, len(sack[0])):
#         if sack[0][i] in sack[1]:
#             item = sack[0][i]
#             items.append(item)
#             if ord(item) < 91:
#                 val = ord(item) - 64
#             else:
#                 val = ord(item) - 70
#             total += val
           
#             break
  
    

