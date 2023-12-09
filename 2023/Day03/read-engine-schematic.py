import re

sum = 0

def has_adjacent_symbol(lines, x_index, y_index, number):
    length = len(str(number))
    min_x = max(0,x_index-1)
    max_x = lambda line: min(x_index+length+1,len(line))
    min_y = max(0,y_index-1)
    max_y = min(y_index+2,len(lines))
    subgrid = map(lambda line: line[min_x:max_x(line)], lines[min_y:max_y])
    #print("----------------")
    #print("subgrid\n" + '\n'.join(subgrid))
    for line in subgrid:
        symbols = re.findall(r'[^\d\.\s]', line)
        if symbols:
            print(str(number) + " has symbols found " + ''.join(symbols))
            return True
    print(str(number) + " no symbols found ")
    return False


with open('2023/Day03/input.txt') as f:
    lines = f.readlines()
    for y_index, line in enumerate(lines):
        print("++++++++")
        print("Line " + str(y_index))
        print("++++++++")
        x_index=0
        numbers = map(int, re.findall(r'\d+', line))
        for number in numbers:
            x_index = line.index(str(number), x_index)
            symbol_found = has_adjacent_symbol(lines, x_index, y_index, number)
            if (symbol_found):
                sum += number
                print(str(sum))
            x_index = min(len(line), x_index+len(str(number)))

