import os

my_file = open("expense.txt", "r")
expenses = my_file.readlines()

expenses = [x.strip() for x in expenses]

for i in range(0, len(expenses) - 1):
    for j in range((i + 1), len(expenses) -1):
        if int(expenses[i]) + int(expenses[j]) == 2020:
            prod = int(expenses[i]) * int(expenses[j])


print(prod)