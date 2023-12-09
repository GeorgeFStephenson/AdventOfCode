import re

max_red = 12
max_green = 13
max_blue = 14

sum_part1 = 0
sum_part2 = 0

def get_game_id(header):
    id = int(re.findall(r'\d+', header)[0])
    return id

def is_game_possible(game):
    rounds = game.split('; ')
    for round in rounds:
        colours = round.split(', ')
        for colour in colours:
            number = int(re.findall(r'\d+', colour)[0])
            if "red" in colour and number > max_red:
                print("red is " + str(number))
                return False
            if "green" in colour and number > max_green:
                print("green is " + str(number))
                return False
            if "blue" in colour and number > max_blue:
                print("blue is " + str(number))
                return False
    return True

def calculate_game_power(game):
    game_power = 1
    min_red = 0
    min_blue = 0
    min_green = 0
    rounds = game.split('; ')
    for round in rounds:
        colours = round.split(', ')
        for colour in colours:
            number = int(re.findall(r'\d+', colour)[0])
            if "red" in colour:
                min_red = max(min_red, number)
            elif "green" in colour:
                min_green = max(min_green, number)
            elif "blue" in colour:
                min_blue = max(min_blue, number)
    print("min red " + str(min_red) + ", min green " + str(min_green) + ", min blue " + str(min_blue))
    min_color_amounts = [min_red, min_blue, min_green]
    for min_color_amount in min_color_amounts:
        if (min_color_amount > 0):
            game_power *= min_color_amount
    print("game power " + str(game_power))
    return game_power

with open('2023/Day02/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        line_parts = line.split(': ')
        header = line_parts[0]
        line_id = get_game_id(header)
        print("game " + str(line_id))
        game = line_parts[1]
        game_possible = is_game_possible(game)
        game_power = calculate_game_power(game)
        sum_part2 += game_power
        if not game_possible:
            print("not possible")
        else:
            print("possible")
            sum_part1 += line_id

print("part 1 answer " + str(sum_part1))
print("part 2 answer " + str(sum_part2))
