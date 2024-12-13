import re
from sympy import Eq, solve
from sympy.abc import a, b

with open('2024/day-13/input.txt') as f:
    lines = list(map(lambda line: list(map(int,re.findall(r'\d+', line))), f.readlines()))

a_buttons = []
b_buttons = []
prizes = []

for idx, line in enumerate(lines):
    type = idx % 4
    if type == 0:
        a_buttons.append(line)
    if type == 1:
        b_buttons.append(line)
    if type == 2:
        prizes.append(line)

total = 0

for a_button, b_button, prize in zip(a_buttons, b_buttons, prizes):
    sol = solve([ Eq(a_button[0]*a + b_button[0]*b, prize[0]+10000000000000),
                Eq(a_button[1]*a + b_button[1]*b, prize[1]+10000000000000)])
    if sol[a].is_Integer and sol[b].is_Integer:
        total += sol[a] * 3 + sol[b]

print("Part 2 Answer:", total)