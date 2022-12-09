import math

fp = open('input.txt', 'r')

modules = fp.readlines()
totalFuel = 0

for module in modules:
    mass = int(module)

    fuel = math.floor((mass/3)) - 2

    totalFuel += fuel



print(totalFuel)
