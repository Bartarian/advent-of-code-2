from aocd import get_data
from dataclasses import dataclass
from itertools import product
import numpy

data = get_data(year=2024, day=7)

testData = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

# allLines = testData.splitlines()
allLines = data.splitlines()

@dataclass
class Equation:
    result : int
    numbers : list[int]
    
allEquations: list[Equation] = []

for line in allLines:
    res, nums = line.split(": ")
    res = int(res)
    nums = [int(x) for x in nums.split(" ")]
    allEquations.append(Equation(res, nums))
    
def getOperations(len):
    return product((0, 1, 2), repeat=len)

total = 0

progressMax = len(allEquations)

for i, eq in enumerate(allEquations):
    print(f"{i}/{progressMax}: {eq}")
    for operation in getOperations(len(eq.numbers) - 1):
        res = eq.numbers[0]
        for ind, op in enumerate(operation):
            if op == 0:
                res += eq.numbers[ind + 1]
            elif op == 1:
                res *= eq.numbers[ind + 1]
            elif op == 2:
                res = int(f"{res}{eq.numbers[ind + 1]}")
        if eq.result == res:
            print(f"Match: {eq.result} = {operation}")
            total += res
            break
    print(f"{total}")

print(total)
