import re

def get_race_times_part1(lines):
    race_times = list(map(int,re.findall(r'\d+', lines[0])))
    return race_times

def get_race_records_part1(lines):
    race_records = list(map(int,re.findall(r'\d+', lines[1])))
    return race_records

def get_race_time_part2(lines):
    numbers = re.findall(r'\d+', lines[0])
    race_time_str = ''.join(numbers)
    race_time = int(race_time_str)
    return race_time

def get_race_record_part2(lines):
    numbers = re.findall(r'\d+', lines[1])
    race_record_str = ''.join(numbers)
    race_record = int(race_record_str)
    return race_record

def get_number_of_ways(race_time, race_record):
    number_of_ways = 0

    for hold_button_time in range(race_time):
        remaining_time = race_time - hold_button_time
        boat_speed = hold_button_time
        distance = boat_speed*remaining_time
        if distance > race_record:
            number_of_ways += 1

    return number_of_ways


with open('2023/Day06/input.txt') as f:
    lines = f.readlines()
    race_times = get_race_times_part1(lines)
    race_records = get_race_records_part1(lines)

    product = 1
    for i in range(len(race_times)):
        race_time = race_times[i]
        race_record = race_records[i]
        number_of_ways = get_number_of_ways(race_time, race_record)
        product *= number_of_ways
    print('part 1 answer ' + str(product))

    race_time = get_race_time_part2(lines)
    race_record = get_race_record_part2(lines)
    number_of_ways = get_number_of_ways(race_time, race_record)
    print('part 2 answer ' + str(number_of_ways))
    