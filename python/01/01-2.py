from collections import Counter
import csv

total_rows = 0
left_list = []
right_list = []
with open("input.txt", "r") as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        left_list.append(int(row[0]))
        right_list.append(int(row[3]))
        total_rows += 1

right_counter = Counter(right_list)
similarity_score = sum(x * right_counter.get(x,0) for x in left_list)

print('sum: {}'.format(similarity_score))