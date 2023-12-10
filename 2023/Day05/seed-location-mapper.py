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

def get_seeds(lines):
    seeds_str = lines[0].split('seeds: ')[1]
    seeds = list(map(int,re.findall(r'\d+', seeds_str)))
    return seeds


def map_value(value, mapper_list: list[Mapper]):
    #print('value ' + str(value))
    for mapper in mapper_list:
        #print(mapper.dest_range_start, mapper.src_range_start, mapper.range_length)
        if value >= mapper.src_range_start and value < (mapper.src_range_start + mapper.range_length):
            mapped_value = mapper.dest_range_start + value-mapper.src_range_start
            #print('value mapped ' + str(mapped_value))
            return mapped_value
    return value

with open('2023/Day05/input.txt') as f:
    lines = f.readlines()
    seeds = get_seeds(lines)
    map_hierarchy:list[list[Mapper]] = []
    map_hierarchy.append(get_mapper_list(lines, 'seed-to-soil'))
    map_hierarchy.append(get_mapper_list(lines, 'soil-to-fertilizer'))
    map_hierarchy.append(get_mapper_list(lines, 'fertilizer-to-water'))
    map_hierarchy.append(get_mapper_list(lines, 'water-to-light'))
    map_hierarchy.append(get_mapper_list(lines, 'light-to-temperature'))
    map_hierarchy.append(get_mapper_list(lines, 'temperature-to-humidity'))
    map_hierarchy.append(get_mapper_list(lines, 'humidity-to-location'))

    seed_transformations = []
    map_results = seeds.copy()
    for mapper_list in map_hierarchy:
        for index, map_result in enumerate(map_results):
            map_results[index] = map_value(map_result, mapper_list)
        seed_transformations.append(map_results.copy())


    print(seed_transformations)
    lowest_location_number = min(map_results)
    print('lowest_location_number ' + str(lowest_location_number))
            
