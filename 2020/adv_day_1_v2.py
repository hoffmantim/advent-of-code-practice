import os

my_file = open("expense.txt", "r")
expenses = my_file.readlines()

expenses = [int(x.strip()) for x in expenses]

for i in range(0, len(expenses) - 1):
    for j in range((i + 1), len(expenses) - 1):
        for k in range((j+1), len(expenses) - 1):
            if (expenses[i]) + (expenses[j]) + (expenses[k])== 2020:
                prod = (expenses[i]) * (expenses[j]) * (expenses[k])


print(prod)