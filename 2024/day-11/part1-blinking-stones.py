import re

with open('2024/day-11/input.txt') as f:
    stones = list(map(int, re.findall(r'\d+', f.readlines()[0])))

blinks = 25

for _ in range(blinks):
    original_stones = list(stones)
    stones_added = 0
    for idx, stone in enumerate(original_stones):
        if stone == 0:
            stones[idx+stones_added] = 1
            continue
        stone_str = str(stone)
        if len(stone_str) % 2 == 0:
            half_stone_str_len = int(len(stone_str)/2)
            first_stone = int(stone_str[:half_stone_str_len])
            second_stone = int(stone_str[half_stone_str_len:])
            stones[idx+stones_added] = first_stone
            stones.insert(idx+stones_added, second_stone)
            stones_added += 1
        else:
            stones[idx+stones_added] = stone*2024

count = len(stones)

print("Result:", count)
