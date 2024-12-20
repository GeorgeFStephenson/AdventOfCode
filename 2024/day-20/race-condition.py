import numpy as np

with open('2024/day-20/input.txt') as f:
    lines = f.readlines()

tiles = [[char for char in line.strip()] for line in lines]
grid = np.array(tiles)
start = np.argwhere(grid == 'S')[0]
end = np.argwhere(grid == 'E')[0]
min_saving = 100
dirs = [[1,0],[0,1],[-1,0],[0,-1]]
cheats = [[2,0],[0,2],[-2,0],[0,-2],[1,1],[1,-1],[-1,1],[-1,-1]]

def get_distance_from_end():
    distance_from_end = []
    current = [end[0],end[1]]
    for dir in dirs:
        if grid[current[0]+dir[0],current[1]+dir[1]] == '.':
            last_dir = dir
            break
    while True:
        distance_from_end.append(current)
        trypos = [current[0]+last_dir[0],current[1]+last_dir[1]]
        if grid[trypos[0],trypos[1]] == '#':
            for trydir in [[last_dir[1],last_dir[0]],[-last_dir[1],-last_dir[0]]]:
                if grid[current[0]+trydir[0],current[1]+trydir[1]] != '#':
                    last_dir = trydir
                    current = [current[0]+trydir[0],current[1]+trydir[1]]
                    break
        else:
            current = trypos
        if grid[current[0],current[1]] == 'S':
            distance_from_end.append(current)
            return distance_from_end
            
distance_from_end = get_distance_from_end()
count = 0
for idx, pos in enumerate(distance_from_end):
    for cheat in cheats:
        if [pos[0]+cheat[0],pos[1]+cheat[1]] in distance_from_end[:idx]:
            saving = idx - 2 - distance_from_end.index([pos[0]+cheat[0],pos[1]+cheat[1]])
            if saving >= min_saving:
                count += 1

print(count)