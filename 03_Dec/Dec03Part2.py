import re

result = 0

with open("03_Dec\\data.txt") as fin:
    data = ""
    for line in fin:
        data += line.rstrip()

arguments = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|don't\(\)|do\(\)", data)

state = True

for argument in arguments:
    if argument == "do()":
        state = True

    elif argument == "don't()":
        state = False
    
    else:
        if state:
            numbers = re.findall('[0-9]{1,3}', argument)
            result += (int(numbers[0]) *  int(numbers[1]))

print( result )