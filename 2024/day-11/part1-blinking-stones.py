import re

with open('2024/day-11/input.txt') as f:
    stones = list(map(int, re.findall(r'\d+', f.readlines()[0])))

stone_iteration_map = {}

def blink_stone(stone, iterations):
    if stone in stone_iteration_map and iterations in stone_iteration_map[stone]:
        return stone_iteration_map[stone][iterations]
    elif stone not in stone_iteration_map:
        stone_iteration_map[stone] = {}
    if stone == 0:
        if iterations == 1:
            stone_iteration_map[stone][1] = 1
            return 1
        stone_iteration_map[stone][iterations] = blink_stone(1, iterations-1)
        return stone_iteration_map[stone][iterations]
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        if iterations == 1:
            return 2
        half_stone_str_len = int(len(stone_str)/2)
        first_stone = int(stone_str[:half_stone_str_len])
        second_stone = int(stone_str[half_stone_str_len:])
        stone_iteration_map[stone][iterations] = blink_stone(first_stone, iterations-1) + blink_stone(second_stone, iterations-1)
        return stone_iteration_map[stone][iterations]
    if iterations == 1:
            stone_iteration_map[stone][1] = 1
            return 1
    stone_iteration_map[stone][iterations] = blink_stone(stone*2024, iterations-1)
    return stone_iteration_map[stone][iterations]

blinks = 75

count = 0
for stone in stones:
    count += blink_stone(stone, blinks)

print("Result:", count)
