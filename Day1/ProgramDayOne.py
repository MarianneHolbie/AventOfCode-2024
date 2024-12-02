#####################
#     Part One      #
#####################
from rapidfuzz.distance.DamerauLevenshtein import similarity

# Create 2 lists of value
col1 = []
col2 = []
with open('input.txt', 'r') as file:
    for lines in file :
        value = lines.split(maxsplit=1)
        if len(value) == 2:
            col1.append(value[0].strip())
            col2.append(value[1].strip())

# Sort value for each list
col1_sort = sorted(col1)
col2_sort = sorted(col2)

# Create list of difference and make sum of the list
distance = [max(int(a), int(b)) - min(int(a), int(b)) for a, b in zip(col1_sort, col2_sort)]
total_distance = sum(distance)
print ("Total distance between two lists:", total_distance)

#####################
#     Part Two      #
#####################

similarity_score = 0
for element in col1_sort:
    counter = col2_sort.count(element)
    similarity_score += int(element) * counter

print("Similarity score is:", similarity_score)
