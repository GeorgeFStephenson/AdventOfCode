import re

sum = 0

rules = {}
updates = []

with open('2024/day-05/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        if '|' in line:
            rule = re.findall(r'\d+', line)
            if rule[0] not in rules:
                rules[rule[0]] = [rule[1]]
            else:
                rules[rule[0]].append(rule[1])
        if ',' in line:
            updates.append(re.findall(r'\d+', line))

for update in updates:
    valid_update = True
    for idx, number in enumerate(update):
        remaining_number_set = set(update[idx+1:])
        if idx == len(update)-1:
            break
        if not number in rules or not remaining_number_set.issubset(rules[number]):
            valid_update = False
            break

    if not valid_update:
        for number in update:
            # the middle number will be the one that only has rules to be before half the other numbers
            len_after_middle = int((len(update)-1)/2)
            if number in rules and len(set(rules[number]).intersection(update)) == len_after_middle:
                sum += int(number)

print("Result:", sum)
