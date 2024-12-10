import numpy as np

with open('2024/day-10/input.txt') as f:
    lines = f.readlines()

grid = [list(map(int, line.strip())) for line in lines]

grid_array = np.array(grid, dtype=np.int8)

x_bound = len(grid_array[0])-1
y_bound = len(grid_array)-1

def find_next_level(current_y, current_x, next_number):
    score = 0
    dirs = [[current_x-1, current_y], [current_x+1, current_y], [current_x, current_y-1], [current_x, current_y+1]]
    for dir in dirs:
        if (0 <= dir[0] <= x_bound) and (0 <= dir[1] <= y_bound) and grid_array[dir[1], dir[0]] == next_number:
            if next_number == 9:
                score += 1
            else:
                score += find_next_level(dir[1], dir[0], next_number+1)
    return score

trailheads = np.argwhere(grid_array == 0)

total = 0
for trailhead in trailheads:
    score = find_next_level(trailhead[0], trailhead[1], 1)
    total += score

print("Result:", total)
