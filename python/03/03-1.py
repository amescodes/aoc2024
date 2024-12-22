import re
import functools

day = "03"
file = "input"

sum = 0
with open(f"python/{day}/{file}.txt", "r") as f:
    all_text = f.read()
    muls = re.findall("mul\(\d{1,3}\,\d{1,3}\)",all_text)
    for mul in muls:
        sum += functools.reduce(lambda x,y: x * y, list(map(int,re.findall("\d{1,3}",mul))))

print('sum of muls: {}'.format(sum))

