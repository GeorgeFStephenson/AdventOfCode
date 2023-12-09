import re
from word2number import w2n

sum = 0
with open('2023/Day01/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        res = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        print(res)
        first_number = res[0]
        last_number = res[-1]
        first_number_digit = str(w2n.word_to_num(first_number))
        last_number_digit = str(w2n.word_to_num(last_number))
        print("First number " + first_number_digit)
        print("Last number " + last_number_digit)
        two_digit_number = first_number_digit + last_number_digit
        print("Two digit number " + two_digit_number)
        sum += int(two_digit_number)
print("Result " + str(sum))
