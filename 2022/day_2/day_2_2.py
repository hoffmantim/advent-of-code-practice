with open("strategy.txt") as f:
    data = f.read()
    contents = data.split("\n")
    for i in range(0, len(contents)):
        contents[i] = contents[i].strip("\n")

scores = {
    "A Z": 8,
    "A Y": 4,
    "A X": 3,
    "B X": 1,
    "B Z": 9,
    "B Y": 5,
    "C Y": 6,
    "C X": 2,
    "C Z": 7
}

total = 0
for turn in contents:
    total += scores[turn]

print(total)