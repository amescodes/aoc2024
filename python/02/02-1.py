day = "02"
file = "input"

safe_count = 0
with open(f"python/{day}/{file}.txt", "r") as f:
    for x in f.readlines():
        row = list(map(int,x.split(' ')))
        
        level_diff = 0
        row_increasing = None
        for prev_level, curr_level in zip(row, row[1:]):
            level_diff = curr_level - prev_level
            if level_diff == 0:
                break

            if row_increasing == None:
                row_increasing = level_diff > 0
            elif (row_increasing and level_diff < 0) or (row_increasing == False and level_diff > 0):
                break

            level_diff_count = abs(level_diff)
            if level_diff_count > 3 or level_diff_count < 1:
                break
        else:
            safe_count += 1
            continue


print('safe reports: {}'.format(safe_count))

