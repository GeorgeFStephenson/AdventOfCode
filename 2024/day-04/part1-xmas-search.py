import re

count = 0
search_word = "XMAS"
search_word_len = len(search_word)
vectors = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]

with open('2024/day-04/input.txt') as f:
    rows = list(map(lambda line: re.findall(r'[A-Z]+', line)[0], f.readlines()))

for y_idx, row in enumerate(rows):
    for x_idx, letter in enumerate(row):
        if letter != search_word[0]:
            continue
        for vector in vectors:
            x_dir = vector[0]
            y_dir = vector[1]
            search_word_range = search_word_len-1
            within_x_bound = 0 <= x_idx+(x_dir*search_word_range) <= len(row)-1
            within_y_bound = 0 <= y_idx+(y_dir*search_word_range) <= len(rows)-1

            if not within_x_bound or not within_y_bound:
                continue

            letters_matched = 1
            for search_idx, search_letter in enumerate(search_word[1:]):
                search_letter_number = search_idx+1
                match_found = rows[y_idx+(y_dir*search_letter_number)][x_idx+(x_dir*search_letter_number)] == search_letter
                if not match_found:
                    break
                letters_matched += 1
            if letters_matched == search_word_len:
                count += 1

print("Result:", count)
