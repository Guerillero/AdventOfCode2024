
# Check if the report either switches direction at all or is steady
# if neither happen return True
def checkWobble(report):
    if report[0] == report[1]:
        # steady
        return False
    
    elif report[0] < report[1]:
        # increase
        for i in range(1, len(report)):
            if report[i] > report[i-1]:
                if i == len(report) - 1:
                    return True
            else:
                return False
    
    else:
        # decrease
        for i in range(1, len(report)):
            if report[i] < report[i-1]:
                if i == len(report) - 1:
                    return True
            else:
                return False

# helper function to calculate distance between two numbers
def _dist(a, b):
    if a > b:
        return a - b
    else:
        return b - a


# check if the jumps are too big
def checkJump(report):
    for i in range(1, len(report)):
            if _dist(report[i], report[i-1]) <= 3:
                if i == len(report) - 1:
                    return True
            else:
                return False
    
            


#Globals
reports = []
safeCount = 0

# read in reports, cast as int, append to global list to make 2D array
for line in open("02_Dec\\data.txt"):
    a = []

    for entry in line.split():
        a.append(int(entry))
    
    reports.append(a)


# check each report for wobble and jump
for report in reports:
    if checkWobble(report) & checkJump(report):
        safeCount += 1

print(safeCount)