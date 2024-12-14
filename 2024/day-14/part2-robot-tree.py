import re
import copy

with open('2024/day-14/input.txt') as f:
    lines = list(map(lambda line: list(map(int,re.findall(r'-?\d+', line))), f.readlines()))

class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

max_x:int = 100
max_y:int = 102
half_x = int(max_x/2)
half_y = int(max_y/2)

empty_grid = []
for y in range(max_y+1):
    line = []
    for x in range(max_x+1):
        line.append(0)
    empty_grid.append(line)

robots = []
for line in lines:
    robot = Robot(line[0], line[1], line[2], line[3])
    robots.append(robot)

seconds = 0
tree_length = 4
christmas_tree = False
max_add_y = 1
while not christmas_tree:
    seconds += 1
    grid = copy.deepcopy(empty_grid)
    for robot in robots:
        robot.x = (robot.x + robot.vx) % (max_x+1)
        robot.y = (robot.y + robot.vy) % (max_y+1)
        if seconds >= 8000:
            grid[robot.y][robot.x] = 1

    if seconds < 8000:
        continue

    for robot in robots:
        if not (tree_length-1 <= robot.x <= max_x-(tree_length-1) and robot.y <= max_y-(tree_length-1)):
            continue
        for add_y in range(1,tree_length):
            if grid[robot.y+add_y][robot.x-add_y] == 0 or grid[robot.y+add_y][robot.x+add_y] == 0:
                break
            if add_y > max_add_y:
                max_add_y = add_y
                print("new max tree", max_add_y)
            if add_y == tree_length-1:
                christmas_tree = True

print("Part 2 Result:", seconds)
    
