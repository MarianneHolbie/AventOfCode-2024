#####################
#     Part One      #
#####################

count = 0

def is_valid_report(report):
    # list of int
    numbers = list(map(int, line.strip().split()))

    # calculate diff for each consecutive numbers
    diffs = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]

    if not all(1 <= abs(d) <= 3 for d in diffs):
        return False

    # verify increasing or decreasing order
    is_increase = all(d > 0 for d in diffs)
    is_decrease = all(d < 0 for d in diffs)

    return is_increase or is_decrease

with open('input.txt', 'r') as file:
    for line in file :
        if is_valid_report(line):
            count += 1

print("Safe reports:", count)
