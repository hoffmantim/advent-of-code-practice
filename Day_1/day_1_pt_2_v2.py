import math

fp = open('input.txt', 'r')

modules = fp.readlines()
masses = []
totalFuel = 0

for module in modules:
    mass = int(module)

    masses.append(mass)


def recursiveHelper(num):
    d = num // 3 - 2
    if d <= 0:
        return 0
    return d + recursiveHelper(d)




print(sum(map(recursiveHelper, masses)))
