

with open('2023/Day08/input.txt') as f:
    lines = f.readlines()
    pattern = list(filter(lambda x: x in ['L','R'], lines[0]))
    nodes = dict()
    for line in lines[2:]:
        node_name = line[:3]
        left_node = line[7:10]
        right_node = line[12:15]
        nodes[node_name] = [left_node, right_node]

    current_node = 'AAA'
    steps = 0
    while current_node != 'ZZZ':
        print('steps ' + str(steps))
        for direction in pattern:
            next_instruction = nodes[current_node]
            if direction == 'L':
                current_node = next_instruction[0]
            else:
                current_node = next_instruction[1]
            steps = steps + 1
            if current_node == 'ZZZ':
                print('answer ' + str(steps))
                break
        