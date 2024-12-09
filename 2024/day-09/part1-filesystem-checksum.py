import re
import itertools

with open('2024/day-09/input.txt') as f:
    number_sequence = f.read().strip()

disk_map = []
current_id = 0
is_file = True
for number_str in number_sequence:
    number = int(number_str)
    if is_file:
        disk_map.extend([current_id] * number)
        current_id += 1
    else:
        disk_map.extend([None] * number)
    is_file = not is_file

for idx, item in enumerate(disk_map):
    if item is not None:
        continue
    swapped_digit = None
    while swapped_digit is None:
        swapped_digit = disk_map.pop()
    disk_map[idx] = swapped_digit

if disk_map[-1] is None:
    disk_map.pop()

total = sum(idx * item for idx, item in enumerate(disk_map))

print("Result:", total)
