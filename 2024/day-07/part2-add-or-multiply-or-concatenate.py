import re

with open('2024/day-07/input.txt') as f:
    lines = list(map(lambda line: list(map(int, re.findall(r'\d+', line))), f.readlines()))

sum = 0

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

for line in lines:
    result = line[0]
    terms = line[1:]
    num_of_operators = len(terms)-1
    num_of_combinations = pow(3,num_of_operators)
    for n in range(num_of_combinations):
        working_total = terms[0]
        combination = ternary(n).zfill(num_of_operators)
        for idx, term in enumerate(terms[1:]):
            if combination[idx] == '1':
                working_total *= term
            elif combination[idx] == '2':
                working_total = int(str(working_total) + str(term))
            else:
                working_total += term
        if working_total == result:
            sum += working_total
            break

print("Result:", sum)
