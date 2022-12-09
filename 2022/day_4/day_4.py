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
    dash0 = section[0].index("-")
    e0min = int(section[0][:dash0])
    e0max = int(section[0][dash0+1:])
    dash1 = section[1].index("-")
    e1min = int(section[1][:dash1])
    e1max = int(section[1][dash1+1:])


    if (e0min <= e1min and e0max >= e1max) or (e0min >= e1min and e0max <= e1max):
        count += 1

print(count)
