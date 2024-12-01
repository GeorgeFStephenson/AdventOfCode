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

class SimilarNumber:
    frequency = 1
    similarityScore = 0
    def __init__(self, number):
        self.number = number

distinctNumsInFirstList = list(set(firstList))
similarityList = []

for number in distinctNumsInFirstList:
    similarNumber = SimilarNumber(number)
    similarNumber.frequency = firstList.count(number)
    secondListOccurences = secondList.count(number)
    similarNumber.similarityScore = number * similarNumber.frequency * secondListOccurences
    similarityList.append(similarNumber)

similarityScores = [sn.similarityScore for sn in similarityList]

totalSimilarityScore = sum(similarityScores)

print("Result:", totalSimilarityScore)
