#####################
#     Part One      #
#####################

import re

total = 0

# pattern
pattern = r'mul\((\d+),(\d+)\)'

with open('input.txt', 'r') as file:
    for line in file :
        matches = re.findall(pattern, line)

        for match in matches:
            result = eval(f'{match[0]} * {match[1]}')
            total += result

print("Total:", total)
