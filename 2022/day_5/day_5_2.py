rows = {
    1: ["B", "Q", "C"],
    2: ["R", "Q", "W", "Z"],
    3: ["B", "M", "R", "L", "V"],
    4: ["C", "Z", "H", "V", "T", "W"],
    5: ["D", "Z", "H", "B", "N", "V", "G"],
    6: ["H", "N", "P", "C", "J", "F", "V", "Q"],
    7: ["D", "G", "T", "R", "W", "Z", "S"],
    8: ["C", "G", "M", "N", "B", "W", "Z", "P"],
    9: ["N", "J", "B", "M", "W", "Q", "F", "P"]
}

with open("moves.txt") as f:
    data = f.read()

moves = data.split("\n")

for move in moves:
    numMove = int(move[move.index(" "):move.index("f")-1])
    nextStr = move[move.index("from"):]
    rowFrom = int(nextStr[nextStr.index(" "):nextStr.index("t")-1])
    lastStr = nextStr[nextStr.index("to"):]
    rowTo = int(lastStr[lastStr.index(" "):])

    stack = rows[rowFrom][-numMove:]
    for box in stack:
        rows[rowTo].append(box)

    for i in range(numMove):
        rows[rowFrom].pop()
    



final = ""
for row in rows:
    final += rows[row].pop()

print(final)