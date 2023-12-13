

import re


with open('2023/Day09/input.txt') as f:
    lines = f.readlines()
    next_values = []
    previous_values = []
    for line in lines:
        numbers = list(map(int,re.findall(r'-?\d+', line)))
        print(numbers)
        end = False
        levels = [numbers]

        while not end:
            previous_level = levels[-1]
            level = []
            for x in range(len(previous_level)-1):
                increase = previous_level[x+1] - previous_level[x]
                level.append(increase)
            levels.append(level)
            if all(x == level[0] for x in level):
                end = True
                
        reversed_levels = list(reversed(levels))
        for index, level in enumerate(reversed_levels):
            increase = level[-1]
            if index < len(reversed_levels)-1:
                next_level = reversed_levels[index+1]
                next_level.append(next_level[-1]+increase)

        next_value = reversed_levels[-1][-1]
        next_values.append(next_value)

        for index, level in enumerate(reversed_levels):
            increase = level[0]
            if index < len(reversed_levels)-1:
                next_level = reversed_levels[index+1]
                next_level.insert(0, next_level[0]-increase)

        previous_value = reversed_levels[-1][0]
        previous_values.append(previous_value)
    
    
print("part 1 answer:")
print(sum(next_values))
print("part 2 answer:")
print(sum(previous_values))