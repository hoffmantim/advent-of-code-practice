from collections import Counter

min = 125730
max = 579381
increasing_digits = []
valid_pw = []

for num in range(min, max):
    digits = [ int(char) for char in str(num) ]
    if sorted(digits) == digits:
        increasing_digits.append(num)



for num in increasing_digits:

    digits = [ int(char) for char in str(num) ]

    mydict = Counter(digits)
    print(mydict)
    for key in mydict: 
        if key == 2:
            valid_pw.append(num)


# xdzprint(valid_pw)