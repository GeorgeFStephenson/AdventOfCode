import re
from typing import List

sign = lambda x: (x > 0) - (x < 0)

def is_safe(numbers: List[int]):
    safe = True
    direction = 0
    for idx in range(len(numbers)-1):
        difference = numbers[idx] - numbers[idx+1]
        abs_difference = abs(difference)
        last_direction = direction
        direction = sign(difference)

        same_direction = last_direction == 0 or direction == last_direction
        within_limits = (1 <= abs_difference <= 3)
        if (not same_direction or not within_limits):
            safe = False
    return safe

def is_safe_with_dampener(numbers: List[int]):
    safe = is_safe(numbers)
    if (safe):
        return safe
    numbers_len = len(numbers)
    for idx in range(numbers_len):
        dampened_numbers = list(numbers)
        dampened_numbers.pop(idx)
        safe = is_safe(dampened_numbers)
        if (safe):
            return safe
    
safe_reports = 0

with open('2024/day-02/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        res = re.findall(r'\d+', line)
        numbers = list(map(int, res))
        safe = is_safe_with_dampener(numbers)
        if (safe):
            safe_reports += 1


print("Result:", safe_reports)
