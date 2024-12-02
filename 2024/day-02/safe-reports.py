import re
import math

sign = lambda x: (x > 0) - (x < 0)

safe_reports = 0

with open('2024/day-02/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        res = re.findall(r'\d+', line)
        numbers = list(map(int, res))
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
        
        if (safe):
            safe_reports += 1


print("Result:", safe_reports)
