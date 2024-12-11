from functools import cache
import re

with open('2024/day-11/input.txt') as f:
    stones = list(map(int, re.findall(r'\d+', f.readlines()[0])))

@cache
def blink_stone(stone, iterations):
    if stone == 0:
        if iterations == 1:
            return 1
        return blink_stone(1, iterations-1)
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        if iterations == 1:
            return 2
        half_stone_str_len = int(len(stone_str)/2)
        first_stone = int(stone_str[:half_stone_str_len])
        second_stone = int(stone_str[half_stone_str_len:])
        return blink_stone(first_stone, iterations-1) + blink_stone(second_stone, iterations-1)
    if iterations == 1:
        return 1
    return blink_stone(stone*2024, iterations-1)

blinks = 25
count = 0
for stone in stones:
    count += blink_stone(stone, blinks)

print("Part 1 Result:", count)

blinks = 75
count = 0
for stone in stones:
    count += blink_stone(stone, blinks)

print("Part 2 Result:", count)