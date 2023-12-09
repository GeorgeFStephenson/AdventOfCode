import re

sum = 0

def find_adjacent_numbers(lines, x_index, y_index):
    min_x = max(0,x_index-1)
    max_x = lambda line: min(x_index+2,len(line))
    min_y = max(0,y_index-1)
    max_y = min(y_index+2,len(lines))
    subgrid = map(lambda line: line[min_x:max_x(line)], lines[min_y:max_y])
    #print("----------------")
    #print("subgrid\n" + '\n'.join(subgrid))
    numbercoords = []
    for subgrid_y, line in enumerate(subgrid):
        numbers_in_line = re.findall(r'\d+', line)
        scan_x = 0
        for number_in_line in numbers_in_line:
            scan_x = line.index(number_in_line, scan_x)
            numbercoords.append([min_x+scan_x, min_y+subgrid_y])
            scan_x += len(number_in_line)
    return numbercoords

def get_number(lines, adjacent_numbers_coord):
    x_index = adjacent_numbers_coord[0]
    y_index = adjacent_numbers_coord[1]
    line = lines[y_index]
    numbers_in_line = re.findall(r'\d+', line)
    scan_x=0
    for number_in_line in numbers_in_line:
        scan_x = line.index(number_in_line, scan_x)
        if x_index >= scan_x and x_index <= scan_x + len(number_in_line):
            return int(number_in_line)
        scan_x += len(number_in_line)


with open('2023/Day03/input.txt') as f:
    lines = f.readlines()
    for y_index, line in enumerate(lines):
        print("++++++++")
        print("Line " + str(y_index))
        print("++++++++")
        x_index=0
        gears = re.findall(r'\*', line)
        for gear in gears:
            x_index = line.index(gear, x_index)
            
            adjacent_numbers_coords = find_adjacent_numbers(lines, x_index, y_index)
            if len(adjacent_numbers_coords) == 2:
                print(''.join(map(lambda x: ''.join(str(x)),adjacent_numbers_coords)))
                number1 = get_number(lines, adjacent_numbers_coords[0])
                print("number1 " + str(number1))
                number2 = get_number(lines, adjacent_numbers_coords[1])
                print("number2 " + str(number2))
                gear_ratio = number1 * number2
                print(str(number1) + " and " + str(number2) + " gear ratio " + str(gear_ratio))
                sum += gear_ratio
                print(str(sum))

            #skip ahead now
            x_index = min(len(line), x_index+1)

print(str(sum))
