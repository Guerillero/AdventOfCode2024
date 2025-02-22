import re

result = 0

with open("03_Dec\\data.txt") as fin:
    data = ""
    for line in fin:
        data += line.rstrip()

funcs = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', data)

for func in funcs:
    numbers = re.findall('[0-9]{1,3}', func)
    result += (int(numbers[0]) *  int(numbers[1]))

print( result )