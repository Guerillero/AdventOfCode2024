# Code to generate soultion of Advent of Code 2024, Dec01 Part2


# Create globals
col1 = []
col2 = []
result = 0

# Read the data file and place the two columns into two separate lists
for line in open("01_Dec\\data.txt"):
    col1.append(line.split()[0])
    col2.append(line.split()[1])

# find the number of times the first column entry appears in the second column
# This is probably the least efficent way to do this
for entry in col1:
    matches = 0
    for i in col2:
        if i == entry:
            matches += 1
    result += (matches * int(entry))

print(result)