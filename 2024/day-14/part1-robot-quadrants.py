import re
import math

with open('2024/day-14/input.txt') as f:
    lines = list(map(lambda line: list(map(int,re.findall(r'-?\d+', line))), f.readlines()))

class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

robots = []
max_x = 100
max_y = 102
half_x = max_x/2
half_y = max_y/2
seconds = 100
quadrants = [0, 0, 0, 0]

def add_to_quadrants(x, y):
    if x < half_x and y < half_y:
        quadrants[0] += 1
        return
    if x < half_x and y > half_y:
        quadrants[1] += 1
        return
    if x > half_x and y < half_y:
        quadrants[2] += 1
        return
    if x > half_x and y > half_y:
        quadrants[3] += 1
        return

for line in lines:
    robot = Robot(line[0], line[1], line[2], line[3])
    robots.append(robot)
    robot.x = (robot.x + robot.vx * seconds) % (max_x+1)
    robot.y = (robot.y + robot.vy * seconds) % (max_y+1)
    add_to_quadrants(robot.x, robot.y)

safety_factor = math.prod(quadrants)

print("Part 1 Result:", safety_factor)
    
