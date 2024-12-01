import re

firstList = []
secondList = []
totalDistance = 0

with open('2024/day-01/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        res = re.findall(r'\d+', line)
        firstNumber = int(res[0])
        firstList.append(firstNumber)
        secondNumber = int(res[1])
        secondList.append(secondNumber)

firstList.sort()
secondList.sort()

for idx, firstListNum in enumerate(firstList):
    secondListNum = secondList[idx]
    absDiff = abs(firstListNum - secondListNum)
    totalDistance += absDiff


print("Result:", totalDistance)
