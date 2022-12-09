with open("bags.txt") as f:
    data = f.read()
    contents = data.split("\n")


rucksacks = []
total = 0

for item in contents:
    middle = (len(item)//2)
    left = item[:middle]
    right = item[middle:]
    rucksacks.append([left, right])

items = []

for sack in rucksacks:
    val = 0
    for i in range(0, len(sack[0])):
        if sack[0][i] in sack[1]:
            item = sack[0][i]
            items.append(item)
            if ord(item) < 91:
                val = ord(item) - 64
            else:
                val = ord(item) - 70
            total += val
           
            break
  
    

print(total)