import re
import itertools

with open('2024/day-09/input.txt') as f:
    input = f.read().strip()

disk_map = []

id = 0
is_file = True
for number_str in input:
    number = int(number_str)

    if is_file:
        for _ in itertools.repeat(None, number):
            disk_map.append(id)
        id += 1
    else:
        for _ in itertools.repeat(None, number):
            disk_map.append(None)
    
    is_file = not is_file

copy_disk_map = list(disk_map)
for idx, item in enumerate(copy_disk_map):
    if idx > len(disk_map)-1:
        break
    if item is None:
        swapped_digit = None
        while swapped_digit is None:
            swapped_digit = disk_map.pop()
        disk_map[idx] = swapped_digit

if disk_map[-1] == None:
    disk_map.pop()

sum = 0
for idx, item in enumerate(disk_map):
    sum += idx * item

print("Result:", sum)
