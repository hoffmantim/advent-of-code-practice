min = 125730
max = 579381
increasing_digits=[]
valid_PW = []
invalid_PW = []
final_PW = []


for num in range(min, max):
    digits = [ int(char) for char in str(num) ]
    if sorted(digits) == digits:
        increasing_digits.append(num)
        

