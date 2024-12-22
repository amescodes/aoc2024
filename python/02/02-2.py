day = "02"
file = "input"

def checkLevel(row):
    row_increasing = None
    for prev_level, curr_level in zip(row, row[1:]):
        level_diff = curr_level - prev_level
        if level_diff == 0:
            return False
        if row_increasing == None:
            row_increasing = level_diff > 0
        elif (row_increasing and level_diff < 0) or (row_increasing == False and level_diff > 0):
            return False
        level_diff_count = abs(level_diff)
        if level_diff_count > 3 or level_diff_count < 1:
            return False
    else:
        return True

rows = []
with open(f"python/{day}/{file}.txt", "r") as f:
    for x in f.readlines():
        rows.append(list(map(int,x.split(' '))))

safe_count = 0
total_rows = len(rows)
dampener_rows = []
for row in rows:
    if checkLevel(row):
        safe_count += 1
    else:
        dampener_rows.append(row)

for row in dampener_rows:
    for index, level in enumerate(row):
        dampened_row = list(row)
        dampened_row.pop(index)
        if checkLevel(dampened_row):
            safe_count += 1
            break

print('safe reports: {} of {} total reports'.format(safe_count,total_rows))