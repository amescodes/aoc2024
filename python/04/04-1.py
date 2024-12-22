import itertools

day = "04"
file = "input"

xmas = ['X','M','A','S']

def checkDir(x,y,x_diff,y_diff):
    return x + x_diff, y + y_diff


total = 0
with open(f"python/{day}/{file}.txt", "r") as f:
    rows = list(map(lambda l: l.replace("\n",""),f.readlines()))
    last_row_index = len(rows) - 1
    last_col_index = len(rows[0]) - 1
    for row_index,row in enumerate(rows):
        row_check_diff = [-1,0,1]
        if row_index < 3:
            row_check_diff.remove(-1)
        elif(row_index > last_row_index - 3):
            row_check_diff.remove(1)
        for col_index, col in enumerate(row):
            col_check_diff = [-1,0,1]
            if col_index < 3:
                col_check_diff.remove(-1)
            elif(col_index > last_col_index - 3):
                col_check_diff.remove(1)

            if col == 'X':
                for dir in list(itertools.product(row_check_diff,col_check_diff)):
                    if dir == (0,0):
                        continue
                    curr_xmas = ['X']
                    last_check_row = row_index
                    last_check_col = col_index
                    while len(curr_xmas) < 4:
                        last_check_row,last_check_col = checkDir(last_check_row,last_check_col,dir[0],dir[1])
                        if last_check_row > last_row_index or last_check_col > last_col_index or last_check_row < 0 or last_col_index < 0:
                            continue
                        curr_xmas.append(rows[last_check_row][last_check_col])
                    if curr_xmas == xmas:
                        total += 1


print('total xmas: {}'.format(total))
