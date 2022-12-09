import operator
ops = { "+": operator.add, "-": operator.sub}

data = open('data.txt', 'r')

steps = data.readlines()
value = 0
valuesList = []
uniqueNums = []
duplicates = []

for step in steps:
  oper = step[0]
  num = step[1:]
  value = ops[oper](value, int(num))
  valuesList.append(value)

valuesList.sort()

print(valuesList)
