

def get_next_step_coords(maze, steps_map, x, y):
    max_x = len(maze[0])-1
    max_y = len(maze)-1
    next_step_coords = []
    if x > 0 and steps_map[y][x-1] == -1:
        west_tile = maze[y][x-1]
        if west_tile in ['-','L','F']:
            next_step_coords.append([x-1,y])
    if x < max_x and steps_map[y][x+1] == -1:
        east_tile = maze[y][x+1]
        if east_tile in ['-','J','7']:
            next_step_coords.append([x+1,y])
    if y > 0 and steps_map[y-1][x] == -1:
        north_tile = maze[y-1][x]
        if north_tile in ['|','7','F']:
            next_step_coords.append([x,y-1])
    if y < max_y and steps_map[y+1][x] == -1:
        south_tile = maze[y+1][x]
        if south_tile in ['|','L','J']:
            next_step_coords.append([x,y+1])
    return next_step_coords



maze = []
with open('2023/Day10/input.txt') as f:
    maze = f.read().splitlines() 

steps_map = []
animal_x = 0
animal_y = 0
for idx, line in enumerate(maze):
    if 'S' in line:
        animal_x = line.index('S')
        animal_y = idx
    points = list(map(lambda x: -1, maze))
    steps_map.append(points)

steps_map[animal_y][animal_x] = 0
max_steps = 0
end = False

while not end:
    increment_max_steps = False
    for y_idx, line in enumerate(steps_map):
        if max_steps in line:
            x_positions = [x_idx for x_idx, x in enumerate(line) if x == max_steps]
            for x_position in x_positions:
                next_steps_coords = get_next_step_coords(maze, steps_map, x_position, y_idx)
                for next_step_coord in next_steps_coords:
                    next_x = next_step_coord[0]
                    next_y = next_step_coord[1]
                    steps_map[next_y][next_x] = max_steps + 1
                    increment_max_steps = True
    if increment_max_steps:
        max_steps += 1
    else:
        end = True

print('part 1 answer:')
print(max_steps)