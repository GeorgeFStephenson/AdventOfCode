import re

with open('2024/day-17/input.txt') as f:
    lines = f.readlines()

newline_idx = lines.index('\n')
a, b, c = [int(re.findall(r'\d+', line)[0]) for line in lines[:newline_idx]]
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
    output.append(str(combo(x) % 8))
def bdv(x):
    global a, b
    b = a // pow(2, combo(x))
def cdv(x):
    global a, c
    c = a // pow(2, combo(x))

instruction_map = { 0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv }

while pointer < len(program)-1:
    opcode, operand = program[pointer:pointer+2]
    increment_pointer = True
    instruction_map[opcode](operand)
    if increment_pointer:
        pointer = pointer + 2
    
result = ','.join(output)
print(result)