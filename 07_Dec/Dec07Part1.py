
def _solve(factors, signs):
    print(factors, signs)
    outcome = int(factors[0])
    for i in range(1, len(factors)):
        if signs[i-1] == "+":
            outcome += int(factors[i])
        else:
            outcome *= int(factors[i])
    return outcome

def _mutate(signs):
    if signs.count("*") == 0:
        signs[0] = "*"
    elif signs.count("*") == 1:
        for i in range(len(signs)):
            if signs[i]  == "*" & len(signs) == 1:
                print("error")
                raise Exception()
            elif signs[i] == "*" & i < len(signs) - 1:
                print("foo")
                signs[i] = "+"
                signs[i + 1] = "*"
            elif signs[i] == "*" & i == len(signs) - 1:
                signs[i] = "+"
                signs[0] = "*"
                signs[1] = "*"
    return signs



def canBeSolved(outcome, factors):
    signs = ["+"] * ( len(factors) - 1 )

    while True:
        if _solve(factors, signs) == outcome:
            return True
        else:
            try:
                signs = _mutate(signs)
            except:
                return False



arguments = []

for line in open("07_Dec\\testData.txt"):
    arguments.append(line.split(":"))


for argument in arguments:
    result = int(argument[0])
    values = argument[1].strip().split()

    print( canBeSolved(result, values) )
