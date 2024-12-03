import re

result = 0

enabled = True

with open('2024/day-03/input.txt') as f:
    lines = f.read()
    regex_matches = re.findall(r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)", lines)
    for match in regex_matches:
        if match[0] == 'do()':
            enabled = True
        elif match[1] == "don't()":
            enabled = False
        elif enabled:
            first_num = int(match[2])
            second_num = int(match[3])
            result += first_num*second_num

print("Result:", result)
