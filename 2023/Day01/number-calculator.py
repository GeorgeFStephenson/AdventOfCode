import re

sum = 0
with open('2023/Day01/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        res = re.findall(r'\d', line)
        print(res)
        firstNumber = res[0]
        lastNumber = res[-1]
        print("First number " + firstNumber)
        print("Last number " + lastNumber)
        twoDigitNumber = firstNumber + lastNumber
        sum += int(twoDigitNumber)
print("Result " + str(sum))
