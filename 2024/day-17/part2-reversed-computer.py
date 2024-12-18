import re

with open('2024/day-17/input.txt') as f:
    lines = f.readlines()

newline_idx = lines.index('\n')
a = 0 
b = 0
c = 0
program = list(map(int, re.findall(r'\d+', lines[newline_idx+1])))
pointer = 0
increment_pointer = True
output=[]

def combo(x):
    if 0 <= x <= 3: return x
    if x == 4: return a
    if x == 5: return b
    if x == 6: return c
    raise ValueError

def adv(x): 
    global a 
    a = a // pow(2, combo(x))
def bxl(x): 
    global b
    b = b ^ x
def bst(x): 
    global b
    b = combo(x) % 8
def jnz(x):
    global a, pointer, increment_pointer
    if a != 0:
        pointer = x
        increment_pointer = False
def bxc(x):
    global b, c
    b = b ^ c
def out(x):
    global output
    output.append(combo(x) % 8)
def bdv(x):
    global a, b
    b = a // pow(2, combo(x))
def cdv(x):
    global a, c
    c = a // pow(2, combo(x))

instruction_map = { 0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv }


def run():
    global pointer, increment_pointer
    while pointer < len(program)-1:
        opcode, operand = program[pointer:pointer+2]
        increment_pointer = True
        instruction_map[opcode](operand)
        if increment_pointer:
            pointer = pointer + 2

success_a_list = [0]
for idx, next_result in enumerate(list(reversed(program))):
    try_a_list = []
    for success_a in success_a_list:
        try_a_list.extend([success_a*8 + n for n in range(8)])
    success = False
    success_a_list = []
    for try_a in try_a_list:
        a = try_a
        b = 0
        c = 0
        pointer = 0
        output=[]
        increment_pointer = True
        run()
        if output[0] == next_result:
            success = True
            success_a_list.append(try_a)

print(min(success_a_list))