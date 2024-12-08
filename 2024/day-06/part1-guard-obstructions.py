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
        
def symbol_to_write(dir):
    match dir:
        case [0,-1]:
            return "^"
        case [1,0]:
            return ">"
        case [0,1]:
            return "v"
        case [-1,0]:
            return "<"
        
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
    original_grid = list(map(lambda line: re.findall(r'[A-Z.#\^]+', line)[0], f.readlines()))

x_bound = len(original_grid[0])-1
y_bound = len(original_grid)-1

start_pos = start_coords(original_grid)
start_symbol = original_grid[start_pos[1]][start_pos[0]]

def check_with_obstruction(grid, start_pos, block_x, block_y):
    new_grid = list(grid)
    new_grid[block_y] = new_grid[block_y][:block_x] + '#' + new_grid[block_y][block_x+1:]
    return check_for_loop(new_grid, start_pos)

def check_for_loop(grid, start_pos):
    previous_dirs = list(map(lambda line: list(map(lambda char: [char], line)), original_grid))
    pos = list(start_pos)
    dir = next_step_dir(start_symbol)

    inside = True
    while inside:
        next_x = pos[0]+dir[0]
        next_y = pos[1]+dir[1]

        if next_x < 0 or next_x > x_bound or next_y < 0 or next_y > y_bound:
            inside = False
            break

        if grid[next_y][next_x] == '#':
            dir = turn_right(dir)
        else:
            pos[0] += dir[0]
            pos[1] += dir[1]

        next_symbol = symbol_to_write(dir)
        if next_symbol in previous_dirs[pos[1]][pos[0]]:
            return True
        else:
            previous_dirs[pos[1]][pos[0]].append(next_symbol)   

    return False
    
def mark_travel(grid, start_pos):
    pos = list(start_pos)
    dir = next_step_dir(start_symbol)

    travel_grid = list(grid)
    travel_grid[pos[1]] = travel_grid[pos[1]][:pos[0]] + 'X' + travel_grid[pos[1]][pos[0]+1:]

    inside = True
    while inside:
        next_x = pos[0]+dir[0]
        next_y = pos[1]+dir[1]

        if next_x < 0 or next_x > x_bound or next_y < 0 or next_y > y_bound:
            inside = False
            break

        if travel_grid[next_y][next_x] == '#':
            dir = turn_right(dir)
        else:
            pos[0] += dir[0]
            pos[1] += dir[1]
            travel_grid[pos[1]] = travel_grid[pos[1]][:pos[0]] + 'X' + travel_grid[pos[1]][pos[0]+1:]

    return travel_grid


# Took me a while to find the right algorithm.
# you know you have entered an infinite loop immediately if you are in the same position and direction
# that you're already been in. No need to count loops or something crazy
# Then we just try obstructing every location the guard visits on their original unobstructed path
marked_travel_grid = mark_travel(original_grid, start_pos)

count = 0
for y_idx, line in enumerate(marked_travel_grid):
    for x_idx, char in enumerate(line):
        if char == "X":
            will_cause_loop = check_with_obstruction(original_grid, start_pos, x_idx, y_idx)
            if will_cause_loop:
                count += 1


print("Result:", count)

