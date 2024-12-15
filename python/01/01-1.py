import csv

left_list = []
right_list = []
with open("input.txt", "r") as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        left_list.append(int(row[0]))
        right_list.append(int(row[3]))

left_list.sort()
right_list.sort()

distance_sum = 0

distance_sum = sum(abs(i-j)for i,j in zip(left_list,right_list))

print('sum: {}'.format(distance_sum))