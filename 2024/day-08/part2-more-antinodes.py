import re

with open('2024/day-08/input.txt') as f:
    lines = list(map(lambda line: re.findall(r'[A-Za-z0-9.]+', line)[0], f.readlines()))

antinode_grid = list(lines)

x_bound = len(lines[0])-1
y_bound = len(lines)-1

satellites = {}

def try_add_antinode(x, y):
    if antinode_grid[y][x] != '#':
            antinode_grid[y] = antinode_grid[y][:x] + '#' + antinode_grid[y][x+1:]

def try_add_all_antinodes(original_x, original_y, x_vector, y_vector):
    # first direction
    x = original_x
    y = original_y
    while 0 <= x <= x_bound and 0 <= y <= y_bound:
        try_add_antinode(x, y)
        x += x_vector
        y += y_vector
    # second direction
    x = original_x
    y = original_y
    while 0 <= x <= x_bound and 0 <= y <= y_bound:
        try_add_antinode(x, y)
        x -= x_vector
        y -= y_vector

for y_idx, line in enumerate(lines):
    for x_idx, char in enumerate(line):
        if re.match(r'[A-Za-z0-9]', char):
            pos = [x_idx, y_idx]
            if char in satellites:
                satellites[char].append(pos)
            else:
                satellites[char] = [pos]

for satellite in satellites:
    pos_list = satellites[satellite]
    for pos_idx, pos in enumerate(pos_list):
        for compare_pos in pos_list[:pos_idx] + pos_list[pos_idx+1:]:
            x_diff = pos[0] - compare_pos[0]
            y_diff = pos[1] - compare_pos[1]
            try_add_all_antinodes(pos[0], pos[1], x_diff, y_diff)

count = 0
for line in antinode_grid:
    count += line.count('#')

print("Result:", count)
