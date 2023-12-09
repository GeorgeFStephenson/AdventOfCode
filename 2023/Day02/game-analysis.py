import re

max_red = 12
max_green = 13
max_blue = 14

sum = 0

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

with open('2023/Day02/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        line_parts = line.split(': ')
        header = line_parts[0]
        line_id = get_game_id(header)
        print("game " + str(line_id))
        game = line_parts[1]
        game_possible = is_game_possible(game)
        if not game_possible:
            print("not possible")
            continue
        print("possible")
        sum += line_id
        print(sum)
