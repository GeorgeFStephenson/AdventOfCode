import re

lowest_location_number = 0

class Mapper:
    def __init__(self, dest_range_start, src_range_start, range_length):
        self.dest_range_start = dest_range_start
        self.src_range_start = src_range_start
        self.range_length = range_length

def get_mapper_list(lines, map_name) -> list[Mapper]:
    mapper_list = []
    map_name_line_str = map_name + ' map:\n'
    map_name_index = lines.index(map_name_line_str)
    map_end_index = 0
    try:
        map_end_index = lines.index('\n', map_name_index+1)
    except:
        map_end_index = len(lines)
    for x in range(map_name_index+1, map_end_index):
        numbers = list(map(int,re.findall(r'\d+', lines[x])))
        mapper_list.append(Mapper(numbers[0], numbers[1], numbers[2]))
    return mapper_list

def get_seeds_part1(lines):
    seeds_str = lines[0].split('seeds: ')[1]
    seeds = list(map(int,re.findall(r'\d+', seeds_str)))
    return seeds

def get_seeds_part2_brute_force(lines):
    seeds = []
    seeds_str = lines[0].split('seeds: ')[1]
    seed_pairs = map(lambda x: x.split(' '), re.findall(r'\d+ \d+', seeds_str))
    for seed_pair in seed_pairs:
        initial_seed = int(seed_pair[0])
        length_of_range = int(seed_pair[1])
        for x in range(length_of_range):
            seeds.append(initial_seed+x)
    return seeds

def get_seed_ranges_part2(lines):
    seed_ranges = []
    seeds_str = lines[0].split('seeds: ')[1]
    seed_pairs = map(lambda x: x.split(' '), re.findall(r'\d+ \d+', seeds_str))
    for seed_pair in seed_pairs:
        initial_seed = int(seed_pair[0])
        length_of_range = int(seed_pair[1])
        seed_ranges.append(range(initial_seed, initial_seed+length_of_range))
    return seed_ranges

def map_value(value, mapper_list: list[Mapper]):
    for mapper in mapper_list:
        if value >= mapper.src_range_start and value < (mapper.src_range_start + mapper.range_length):
            mapped_value = mapper.dest_range_start + value-mapper.src_range_start
            return mapped_value
    return value

def map_range(value_range: range, mapper_list):
    ranges = []
    include_value_range = True
    for mapper in mapper_list:
        src_range = range(mapper.src_range_start, mapper.src_range_start + mapper.range_length)
        dest_range = range(mapper.dest_range_start, mapper.dest_range_start + mapper.range_length)
        if value_range.start > src_range.stop or value_range.stop < src_range.start:
            continue
        elif value_range.start >= src_range.start and value_range.stop <= src_range.stop:
            include_value_range = False
            ranges.append(range(dest_range.start + (value_range.start - src_range.start), dest_range.stop-(src_range.stop-value_range.stop)))
            break
        elif src_range.start > value_range.start and src_range.stop < value_range.stop:
            include_value_range = False
            ranges.append(dest_range)
            ranges.extend(map_range(range(value_range.start, src_range.start),mapper_list))
            ranges.extend(map_range(range(src_range.stop,value_range.stop),mapper_list))
            break
        elif value_range.start < src_range.start:
            clipped_range = range(dest_range.start, dest_range.start + (value_range.stop - src_range.start))
            ranges.append(clipped_range)
            value_range = range(value_range.start, src_range.start)
        elif value_range.stop > src_range.stop:
            clipped_range = range(dest_range.start + (value_range.start - src_range.start), dest_range.stop)
            ranges.append(clipped_range)
            value_range = range(src_range.stop, value_range.stop)
    if include_value_range:
        ranges.append(value_range)
    #print(ranges)
    return ranges


def get_lowest_location_number_part1(seeds, map_hierarchy):
    seed_transformations = []
    map_results = seeds.copy()
    for mapper_list in map_hierarchy:
        for index, map_result in enumerate(map_results):
            map_results[index] = map_value(map_result, mapper_list)
        seed_transformations.append(map_results.copy())
    #print(seed_transformations)
    return min(map_results)

def get_lowest_location_number_part2(seed_ranges, map_hierarchy):
    seed_transformations = []
    map_range_results = seed_ranges.copy()
    for mapper_list in map_hierarchy:
        new_map_range_results = []
        for map_range_result in map_range_results:
            new_map_range_results.extend(map_range(map_range_result, mapper_list))
        map_range_results = new_map_range_results
        print(map_range_results)
        seed_transformations.append(map_range_results.copy())
    #print(seed_transformations)
    return min(list(map(lambda x: x.start, map_range_results)))

with open('2023/Day05/input.txt') as f:
    lines = f.readlines()
    map_hierarchy:list[list[Mapper]] = []
    map_hierarchy.append(get_mapper_list(lines, 'seed-to-soil'))
    map_hierarchy.append(get_mapper_list(lines, 'soil-to-fertilizer'))
    map_hierarchy.append(get_mapper_list(lines, 'fertilizer-to-water'))
    map_hierarchy.append(get_mapper_list(lines, 'water-to-light'))
    map_hierarchy.append(get_mapper_list(lines, 'light-to-temperature'))
    map_hierarchy.append(get_mapper_list(lines, 'temperature-to-humidity'))
    map_hierarchy.append(get_mapper_list(lines, 'humidity-to-location'))

    seeds = get_seeds_part1(lines)
    lowest_location_number = get_lowest_location_number_part1(seeds, map_hierarchy)
    print('part 1 lowest_location_number ' + str(lowest_location_number))
    
    seed_ranges = get_seed_ranges_part2(lines)
    lowest_location_number = get_lowest_location_number_part2(seed_ranges, map_hierarchy)
    print('part 2 lowest_location_number ' + str(lowest_location_number))
