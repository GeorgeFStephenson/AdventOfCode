with open('2024/day-09/input.txt') as f:
    number_sequence = f.read().strip()

disk_map = []
id_count = {}
current_id = 0
is_file = True

for number_str in number_sequence:
    number = int(number_str)
    if is_file:
        disk_map.append([current_id, number])
        id_count[current_id] = number
        current_id += 1
    elif number > 0:
        disk_map.append([None, number])
    is_file = not is_file

reversed_disk_map = list(reversed(disk_map))
max_number = max(id_count.keys())
for last_number in range(max_number, 0, -1):
    last_number_len = id_count[last_number]
    current_last_number_idx = disk_map.index([last_number, last_number_len])

    for idx, header in enumerate(disk_map[:current_last_number_idx]):
        if header[0] == None and header[1] >= last_number_len:
            disk_map[current_last_number_idx] = [None, last_number_len]
            gap_size = header[1]
            disk_map[idx] = [last_number, last_number_len]
            if gap_size > last_number_len:
                disk_map.insert(idx+1, [None, gap_size-last_number_len])
            break

total = 0
position = 0

for item, size in disk_map:
    if item is None:
        position += size
    else:
        for n in range(size):
            total += item * position
            position += 1

print("Result:", total)