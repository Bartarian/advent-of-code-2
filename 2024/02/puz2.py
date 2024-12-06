from aocd import get_data
from enum import Enum
from collections import Counter

data = get_data(year=2024, day=2)

testData = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


total = 0

def computeLevels(input):
    levels = []
    for i, num in enumerate(input[:-1]):
        levels.append(input[i+1] - num)
    return levels

def validateLevels(input):
    if 0 in input:
        return False
    if input[0] > 0:
        ascend = True
    else:
        ascend = False
    for i in input:
        if (i < 0 and ascend) or (i > 0 and not ascend):
            return False
        if i>3 or i <-3:
            return False
    return True
    


for line in data.splitlines():
    numbers = [int(x) for x in line.strip("\n").split(" ")]

    levels = computeLevels(numbers)

    if validateLevels(levels):
        total += 1
    else:
        for i in range(len(numbers)):
            newNumbers = [x for j, x in enumerate(numbers) if j != i]
            levels = computeLevels(newNumbers)
            if validateLevels(levels):
                total += 1
                break
    



print(total)

