from aocd import get, get_data
from copy import deepcopy

data = get_data(year=2024, day=12)

testData1 = """AAAA
BBCD
BBCC
EEEC"""

testData2 = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""

testData3 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

testData4 = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""

testData5 = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""


# data = testData3

fields = []

for lineNum, line in enumerate(data.splitlines()):
    fields.append([])
    for letterNum, letter in enumerate(line):
        fields[lineNum].append({"crop": letter})

numLines = len(fields)
numCols = len(fields[0])

regCounter = 0
lastCrop = ""
allRegions = {}

def getNeighbors(line, col):
    result = []
    if line -1 >= 0:
        result.append([line -1, col])
    if line +1 < numLines:
        result.append([line +1, col])
    if col -1 >= 0:
        result.append([line, col -1])
    if col +1 < numCols:
        result.append([line, col +1])
    return result

def contagion(x, y, crop, region):
    if fields[x][y]["crop"] != crop:
        return (1, 0)
    if "region" in fields[x][y]:
        return (0, 0)
    fields[x][y]["region"] = region
    allRegions[region].append((x, y))
    perimeter = 4
    area = 1
    for neighbor in getNeighbors(x, y):
        perimeter -= 1
        perRet = contagion(neighbor[0], neighbor[1], crop, region)
        perimeter += perRet[0]
        area += perRet[1]
    return (perimeter, area)

region = 0
total = 0

for lineNum, line in enumerate(fields):
    for colNum, plot in enumerate(line):
        if "region" in plot:
            continue
        region += 1
        allRegions[region] = []
        sums = contagion(lineNum, colNum, plot["crop"], region)
        print(f"Region {region}, perimeter {sums[0]} area {sums[1]}")
        total += sums[0] * sums[1]


for line in fields:
    output = ""
    for letter in line:
        output = f"{output}{letter["region"]}"
    print(output)


print(total)

newTotal = 0

for regionNum, region in allRegions.items():
    allCorners = {}
    for plot in region:
        corners = [
            (plot[0], plot[1]),
            (plot[0], plot[1] + 1),
            (plot[0] + 1, plot[1] + 1),
            (plot[0] + 1, plot[1]),
        ]
        for cornerIndex, corner in enumerate(corners):
            if corner not in allCorners:
                allCorners[corner] = []
            allCorners[corner].append(cornerIndex)
    for corner, indexes in deepcopy(allCorners).items():
        if sorted(indexes) in [[0,1], [1,2], [2,3], [0,3], [0,1,2,3]]:
            del allCorners[corner]

    cornerCount = 0
    for corner, indexes in allCorners.items():
        if len(indexes) == 2:
            cornerCount += 2
        else:
            cornerCount += 1
    print(f"Region {regionNum} has area {len(region)} and {cornerCount} corners")
    newTotal += len(region) * cornerCount

print(newTotal)
