

with open('2024/day-12/input.txt') as f:
    lines = f.readlines()

grid = [line.strip() for line in lines]

y_bound = len(grid)-1
x_bound = len(grid[0])-1
visited = []
sides = {}

for line in grid:
    counted_line = []
    for char in line:
        counted_line.append(False)
    visited.append(counted_line)

def in_bounds(x, y):
    return 0 <= x <= x_bound and 0 <= y <= y_bound

def new_side_in_perp_dir(check_x, check_y, check_dir, perp_dir):
    on_edge = True
    while on_edge:
        check_x += perp_dir[0]
        check_y += perp_dir[1]
        if not in_bounds(check_x, check_y):
            on_edge = False
            break
        if grid[check_y][check_x] != grid[y][x]:
            on_edge = False
            break
        if in_bounds(check_x+check_dir[0], check_y+check_dir[1]) and grid[check_y+check_dir[1]][check_x+check_dir[0]] == grid[y][x]:
            #gone inside region, not same side
            on_edge = False
            break
        if [check_x, check_y, check_dir] in sides[region]:
            return False
    return True

def new_side(x, y, check_dir, region):
    if [x,y,check_dir] in sides[region]:
        return False
    perp_dir_1 = [check_dir[1], check_dir[0]]
    perp_dir_2 = [-check_dir[1], -check_dir[0]]

    if new_side_in_perp_dir(x, y, check_dir, perp_dir_1) and new_side_in_perp_dir(x, y, check_dir, perp_dir_2):
        return True
    else:
        return False

def visit(x,y, region):
    if visited[y][x]:
        return [0,0]
    visited[y][x] = True
    area = 1
    symbol = grid[y][x]
    check_dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for check_dir in check_dirs:
        if not in_bounds(x+check_dir[0], y+check_dir[1]):
            if new_side(x, y, check_dir, region):
                sides[region].append([x, y, check_dir])
            continue
        if grid[y+check_dir[1]][x+check_dir[0]] != symbol:
            if new_side(x, y, check_dir, region):
                sides[region].append([x, y, check_dir])
            continue
        if visited[y+check_dir[1]][x+check_dir[0]]:
            continue
        dir_area = visit(x+check_dir[0], y+check_dir[1], region)
        area += dir_area
    return area

total = 0
region = 0

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if not visited[y][x]:
            symbol = grid[y][x]
            region += 1
            sides[region] = []
            area = visit(x, y, region)
            sides_count = len(sides[region])
            total += area*sides_count

print("Part 2 Answer:", total)