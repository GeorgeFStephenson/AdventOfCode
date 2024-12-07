import re

def next_step_dir(symbol):
    match symbol:
        case "^":
            return [0,-1]
        case ">":
            return [1,0]
        case "v":
            return [0,1]
        case "<":
            return [-1,0]
        
def turn_right(coords):
    match coords:
        case [0,-1]:
            return [1,0]
        case [1,0]:
            return [0,1]
        case [0,1]:
            return [-1,0]
        case [-1,0]:
            return [0,-1]
        
def start_coords(lines):
    for y_idx, line in enumerate(lines):
        for x_idx, char in enumerate(line):
            if char in ['^','>','v','<']:
                return [x_idx,y_idx]

with open('2024/day-06/input.txt') as f:
    lines = list(map(lambda line: re.findall(r'[A-Z.#\^]+', line)[0], f.readlines()))


x_bound = len(lines[0])-1
y_bound = len(lines)-1

pos = start_coords(lines)
symbol = lines[pos[1]][pos[0]]
dir = next_step_dir(symbol)
lines[pos[1]] = lines[pos[1]][:pos[0]] + 'X' + lines[pos[1]][pos[0]+1:]

inside = True
while inside:
    next_x = pos[0]+dir[0]
    next_y = pos[1]+dir[1]

    if next_x < 0 or next_x > x_bound or next_y < 0 or next_y > y_bound:
        inside = False
        break

    if lines[next_y][next_x] == '#':
        dir = turn_right(dir)
    else:
        pos[0] += dir[0]
        pos[1] += dir[1]
        lines[pos[1]] = lines[pos[1]][:pos[0]] + 'X' + lines[pos[1]][pos[0]+1:]

count = 0
for line in lines:
    count += line.count('X')
        

print("Result:", count)
