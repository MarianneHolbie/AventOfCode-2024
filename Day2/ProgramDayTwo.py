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


#####################
#     Part Two      #
#####################

def is_valid_sequence(numbers):

    diffs = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]

    if all(1 <= abs(d) <= 3 for d in diffs):
        return all(d > 0 for d in diffs) or all(d < 0 for d in diffs)
    return False


def is_safe_with_removal(line):
    numbers = list(map(int, line.strip().split()))

    if is_valid_sequence(numbers):
        return True

    for idx in range(len(numbers)):
        new_numbers = numbers[:idx] + numbers[idx+1:]
        if is_valid_sequence(new_numbers):
            return True

    return False


count = 0
with open('input.txt', 'r') as f:
    for line in f:
        if is_safe_with_removal(line):
            count += 1

print("New safe count:", count)
