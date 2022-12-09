with open("strategy.txt") as f:
    data = f.read()
    contents = data.split("\n")
    for i in range(0, len(contents)):
        contents[i] = contents[i].strip("\n")

scores = {
    "A Z": 3,
    "A Y": 8,
    "A X": 4,
    "B X": 1,
    "B Z": 9,
    "B Y": 5,
    "C Y": 2,
    "C X": 7,
    "C Z": 6
}

total = 0
for turn in contents:
    total += scores[turn]

print(total)