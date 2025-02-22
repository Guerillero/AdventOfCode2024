# Code to generate soultion of Advent of Code 2024, Dec01 Part1


# Create globals
col1 = []
col2 = []
result = 0

# Read the data file and place the two columns into two separate lists
for line in open("01_Dec\\data.txt"):
    col1.append(line.split()[0])
    col2.append(line.split()[1])

# Sort the two columns
col1.sort()
col2.sort()

for i in range(len(col1)):
    # cast strings int ints
    data = [int(col1[i]), int(col2[i])]

    # Find distance between two numbers
    if data[0] >= data[1]:
        result += (data[0] - data[1]) 
    else:
        result += (data[1] - data[0])

print(result)