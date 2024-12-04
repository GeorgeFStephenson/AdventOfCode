import re

count = 0
search_word = "MAS"
search_word_len = len(search_word)
search_word_range = search_word_len-1
vectors = [[1,1],[-1,-1]]

with open('2024/day-04/input.txt') as f:
    rows = list(map(lambda line: re.findall(r'[A-Z]+', line)[0], f.readlines()))

def within_bounds(x, y):
    within_y_bound = 0 <= y <= len(rows)-1
    if not within_y_bound:
        return False
    within_x_bound = 0 <= x <= len(rows[y])-1
    return within_x_bound

def word_found(x_idx, y_idx, x_dir, y_dir):
    if not within_bounds(x_idx, y_idx):
        return False

    first_letter = rows[y_idx][x_idx]
    if first_letter != search_word[0]:
        return False
    
    if not within_bounds(x_idx+(x_dir*search_word_range), y_idx+(y_dir*search_word_range)):
        return False

    for search_idx, search_letter in enumerate(search_word[1:]):
        search_letter_number = search_idx+1
        match_found = rows[y_idx+(y_dir*search_letter_number)][x_idx+(x_dir*search_letter_number)] == search_letter
        if not match_found:
            return False
    return True

for y_idx, row in enumerate(rows):
    for x_idx, letter in enumerate(row):
        for vector in vectors:
            x_dir = vector[0]
            y_dir = vector[1]
            if not word_found(x_idx, y_idx, x_dir, y_dir):
                continue

            # these are the two possible cross patterns
            if word_found(x_idx+x_dir*2, y_idx, -x_dir, y_dir) or word_found(x_idx, y_idx+y_dir*2, x_dir, -y_dir):
                count+=1        

print("Result:", count)
