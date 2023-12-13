import math
import sys
import time


def choose_path(direction, current_node, nodes_dict):
    next_instruction = nodes_dict[current_node]
    if direction == 'L':
        return next_instruction[0]
    else:
        return next_instruction[1]
    


with open('2023/Day08/input.txt') as f:
    lines = f.readlines()
    pattern = list(filter(lambda x: x in ['L','R'], lines[0]))
    nodes_dict = dict()
    nodes = []
    for line in lines[2:]:
        node_name = line[:3]
        left_node = line[7:10]
        right_node = line[12:15]
        nodes.append(node_name)
        nodes_dict[node_name] = [left_node, right_node]

    current_nodes = list(filter(lambda x: x[2] == 'A', nodes)).copy()
    steps_to_z = []

    for current_node in current_nodes:
        end = False
        steps = 0
        while not end:
            for direction in pattern:
                current_node = choose_path(direction, current_node, nodes_dict)
                steps = steps + 1
                if current_node[2] == 'Z':
                    steps_to_z.append(steps)
                    end = True
    

    lcm = math.lcm(*steps_to_z)
    print(lcm)
        
# I eventually realised you're suppose to calculate the minimum steps take to reach Z for each starting point
# and then calculate the least common multiple