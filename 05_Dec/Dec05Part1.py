# Check if a group of pages meets all of the conditions
def checkConds(pages, conds):
    for cond in conds:
        if (cond[0] in pages) & (cond[1] in pages):
            if (pages.index(cond[0]) < pages.index(cond[1])):
                True
            else:
                return False
        
    return True


# Find and return the middle page
# Please let there not be even numbers in this list
def middle (pages):
    return int( (pages[ int((len(pages) - 1)/2) ] ) )


# Globals
data = []
conditions = []
count = 0


for line in open("05_Dec\\data.txt"):
    data.append(line.rstrip().split(','))

for line in open("05_Dec\\rules.txt"):
    conditions.append(line.rstrip().split('|'))


for pages in data:
    if checkConds(pages, conditions):
        count += middle(pages)

print(count)