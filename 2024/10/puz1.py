from aocd import get_data
import numpy

data = get_data(year=2024, day=10)

testData = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

# data = testData

lineNum = len(data.splitlines())
colNum = len(data.splitlines()[0])

puzzleMap = numpy.zeros(shape=(lineNum, colNum), dtype=numpy.uint8)

for lineN, line in enumerate(data.splitlines()):
    for digitN, digit in enumerate(line):
        puzzleMap[lineN][digitN] = int(digit)

print(puzzleMap)

def calcTrailPoints(startPoint):
    level = puzzleMap[startPoint[0], startPoint[1]]
    if level == 9:
        return [startPoint]

    nextPoints = []
    validEnds = []
    if startPoint[0] - 1 >= 0:
        nextPoints.append([startPoint[0] - 1, startPoint[1]])
    if startPoint[0] + 1 < lineNum:
        nextPoints.append([startPoint[0] + 1, startPoint[1]])
    if startPoint[1] - 1 >= 0:
        nextPoints.append([startPoint[0], startPoint[1] - 1])
    if startPoint[1] + 1 < colNum:
        nextPoints.append([startPoint[0], startPoint[1] + 1])

    for point in nextPoints:
        if puzzleMap[point[0], point[1]] == level + 1:
            validEnds += calcTrailPoints(point)

    return validEnds

total = 0

for line in range(lineNum):
    for col in range(colNum):
        allEnds = []
        if puzzleMap[line][col] != 0:
            continue
        for point in calcTrailPoints([line, col]):
            if tuple(point) not in allEnds:
                allEnds.append(tuple(point))
        total += len(allEnds)

print(total)
