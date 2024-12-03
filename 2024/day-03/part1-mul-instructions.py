import re

result = 0

with open('2024/day-03/input.txt') as f:
    lines = f.read()
    regex_matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', lines)
    for number_pair in regex_matches:
        first = int(number_pair[0])
        second = int(number_pair[1])
        result += first*second

print("Result:", result)
