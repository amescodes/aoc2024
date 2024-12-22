import re
import functools

day = "03"
file = "input"

def removeDont(input:str):
    return input.split("don't()").pop(0)

sum = 0
with open(f"python/{day}/{file}.txt", "r") as f:
    all_text = f.read()
    dos_and_donts = all_text.split("do()")
    dos = list(map(removeDont,dos_and_donts))
    for do in dos:
        muls = re.findall("mul\(\d{1,3}\,\d{1,3}\)",do)
        for mul in muls:
            sum += functools.reduce(lambda x,y: x * y, list(map(int,re.findall("\d{1,3}",mul))))

print('sum of muls: {}'.format(sum))

