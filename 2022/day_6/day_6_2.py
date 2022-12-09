with open("sequence.txt") as f:
    data = f.read()


def isUnique(st):
    char_set = [False] * 128

    for i in range (0, len(st)):
        val = ord(st[i])
        if char_set[val]:
            return Fals
        char_set[val] = True
    
    return True

for i in range(13, len(data)):
    sequence = data[i-13:i+1]
    
    # print(sequence)
    if isUnique(sequence):
        print(i+1)
        break
        

print("end")