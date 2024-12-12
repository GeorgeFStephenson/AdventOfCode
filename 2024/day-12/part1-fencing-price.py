

with open('2024/day-12/input.txt') as f:
    lines = f.readlines()

grid = [line.strip() for line in lines]

y_bound = len(grid)-1
x_bound = len(grid[0])-1
visited = []

for line in grid:
    counted_line = []
    for char in line:
        counted_line.append(False)
    visited.append(counted_line)

def visit(x,y):
    if visited[y][x]:
        return [0,0]
    visited[y][x] = True
    area = 1
    perimeter = 0
    symbol = grid[y][x]
    dirs = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
    for dir in dirs:
        if not (0 <= dir[0] <= x_bound and 0 <= dir[1] <= y_bound):
            perimeter += 1
            continue
        if grid[dir[1]][dir[0]] != symbol:
            perimeter += 1
            continue
        if visited[dir[1]][dir[0]]:
            continue
        (dir_area, dir_perimeter) = visit(dir[0], dir[1])
        area += dir_area
        perimeter += dir_perimeter
    return (area, perimeter)

total = 0

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if not visited[y][x]:
            (area, perimeter) = visit(x, y)
            total += area*perimeter

print("Part 1 Answer:", total)