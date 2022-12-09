with open("sections.txt") as f:
    data = f.read()
    contents = data.split("\n")

sections = []
for item in contents:
   sections.append(item.split(","))

# for each item, find index of "-", create two substrings, one before & one after
# e1_min, e1_max
# e2_min, e2_max
count = 0
for section in sections:
    e0 = []
    e1 = []
    dash0 = section[0].index("-")
    e0min = int(section[0][:dash0])
    e0max = int(section[0][dash0+1:])
    for num in range(e0min, e0max+1):
        e0.append(num)
    dash1 = section[1].index("-")
    e1min = int(section[1][:dash1])
    e1max = int(section[1][dash1+1:])
    for num in range(e1min, e1max + 1):
        e1.append(num)
    
    if any(item in e1 for item in e0):
        count += 1


print(count)
