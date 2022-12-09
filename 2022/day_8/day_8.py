totalVisibleTrees = 0

with open("trees.txt") as f:
    data = f.readlines()

trees = []
for row in data:
    new_row = []
    temp_row = row.strip("\n")
    for digit in temp_row:
        new_row.append(int(digit))
    trees.append(new_row)

# for row in trees:
#     totalVisibleTrees += 2
# totalVisibleTrees -= 2
# for tree in trees[0]:
#     totalVisibleTrees += 2
# totalVisibleTrees -= 2


def horiz(row):
    count = 0
    maxLeft = row[0]
    maxRight = row[-1]

    for i in range(0, len(row)):
        if row[i] >= 9 or maxLeft >= 9:
            break
        elif row[i] > maxLeft:
            count += 1
            maxLeft = row[i]

    for i in range(len(row)-1, 0, -1):
        if row[i] >= 9 or maxRight >= 9:
            break
        elif row[i] > maxRight:
            count += 1
            maxRight = row[i]

    return count

def vertical(column):
    global trees
    count = 0
    maxTop = trees[0][column]
    maxBot = trees[-1][column]

    for i in range(0, len(trees)):
        if trees[i][column] >= 9 or maxTop >=9:
            break
        elif trees[i][column] > maxTop:
            count += 1
            maxTop = trees[i][column]
    
    for i in range(len(trees[i])-1, 0, -1):
        if trees[i][column] >= 9 or maxBot >=9:
            break
        elif trees[i][column] > maxBot:
            count += 1
            maxTop = trees[i][column]

    return count





visTrees = []
for row in trees:
    visTrees.append(horiz(row))

for column in trees[0]:
    visTrees.append(vertical(column))

print(len(visTrees))
print(visTrees)


for num in visTrees:
    totalVisibleTrees += num

print(totalVisibleTrees)