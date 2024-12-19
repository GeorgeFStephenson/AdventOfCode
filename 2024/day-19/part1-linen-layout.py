from functools import cache

with open('2024/day-19/input.txt') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

patterns = set(lines[0].split(', '))
designs = lines[2:]
pattern_max_len = max(map(len, patterns))

@cache
def get_subdesigns(design):
    count = 0
    for pattern_len in reversed(range(1, min(len(design)+1,pattern_max_len+1))):
        sub_design = design[:pattern_len]
        if sub_design in patterns:
            if pattern_len == len(design):
                count += 1
            else:
                count += get_subdesigns(design[pattern_len:])
    return count

count = 0

for design in designs:
    can_start = False
    for i in range(1, min(len(design)+1,pattern_max_len+1)):
        if design[:i] in patterns:
            can_start = True
            break
    if not can_start:
        continue
    can_start = False
    for i in range(1, min(len(design)+1,pattern_max_len+1)):
        if design[-i:] in patterns:
            can_start = True
            break
    if not can_start:
        continue

    count += get_subdesigns(design)

print(count)