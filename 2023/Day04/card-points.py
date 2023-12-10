import re

sum = 0

def find_my_winning_numbers(my_numbers, winning_numbers):
    my_winning_numbers = []
    for num in my_numbers:
        if num in winning_numbers:
            my_winning_numbers.append(num)
    return my_winning_numbers

with open('2023/Day04/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        line_parts = line.split(': ')[1].split(' | ')
        winning_numbers_str = line_parts[0]
        my_numbers_str = line_parts[1]
        winning_numbers = re.findall(r'\d+', winning_numbers_str)
        my_numbers = re.findall(r'\d+', my_numbers_str)

        my_winning_numbers = find_my_winning_numbers(my_numbers, winning_numbers)
        print('my winning numbers ' + ', '.join(map(str,my_winning_numbers)))
        if (my_winning_numbers):
            card_score = 2**(len(my_winning_numbers)-1)
            sum += card_score
        print(str(sum))


