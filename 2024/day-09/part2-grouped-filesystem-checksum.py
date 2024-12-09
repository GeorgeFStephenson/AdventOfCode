import re
import itertools

def find_gap_length(disk_map, start_idx):
    gap_length = 1
    next_digit = None
    while next_digit is None and start_idx+gap_length <= len(disk_map)-1:
        next_digit = disk_map[start_idx+gap_length]
        if next_digit is None:
            gap_length += 1
    return gap_length

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

for last_number in range(max(filter(lambda x: x is not None, disk_map)), 0, -1):
    last_number_len = disk_map.count(last_number)

    gap_idx = disk_map.index(None)
    while gap_idx < disk_map.index(last_number):
        gap_len = find_gap_length(disk_map, gap_idx)
        if gap_len < last_number_len:
            gap_idx = disk_map.index(None, gap_idx+gap_len)
        else:
            while last_number in disk_map:
                disk_map[disk_map.index(last_number)] = None
            for n in range(last_number_len):
                disk_map[gap_idx+n] = last_number            
            break

total = 0

for idx, item in enumerate(disk_map):
    if item is not None:
        total += item * idx

print("Result:", total)
