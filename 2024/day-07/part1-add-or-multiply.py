import re

with open('2024/day-07/input.txt') as f:
    lines = list(map(lambda line: list(map(int, re.findall(r'\d+', line))), f.readlines()))

sum = 0

for line in lines:
    result = line[0]
    terms = line[1:]
    num_of_operators = len(terms)-1
    num_of_combinations = pow(2,num_of_operators)
    for n in range(num_of_combinations):
        working_total = terms[0]
        combination = bin(n)[2:].zfill(num_of_operators)
        for idx, term in enumerate(terms[1:]):
            if combination[idx] == '1':
                working_total *= term
            else:
                working_total += term
        if working_total == result:
            sum += working_total
            break

print("Result:", sum)
