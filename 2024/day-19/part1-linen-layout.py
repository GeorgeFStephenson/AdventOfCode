
with open('2024/day-19/input.txt') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

patterns = set(lines[0].split(', '))
designs = lines[2:]
pattern_max_len = max(map(len, patterns))

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

    sub_designs = [design]
    failed_designs = set()
    while sub_designs:
        sub_design = sub_designs.pop()
        for pattern_len in reversed(range(1, min(len(sub_design)+1,pattern_max_len+1))):
            sub_sub_design = sub_design[:pattern_len]
            if sub_sub_design in failed_designs:
                continue
            if sub_sub_design in patterns:
                if pattern_len == len(sub_design):
                    count += 1
                    sub_designs.clear()
                    break
                elif sub_design[pattern_len:] not in sub_designs and sub_design[pattern_len:] not in failed_designs:
                    sub_designs.append(sub_design[pattern_len:])
            else:
                failed_designs.add(sub_sub_design)


print(count)