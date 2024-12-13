from aocd import get, get_data

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
        sums = contagion(lineNum, colNum, plot["crop"], region)
        print(f"Region {region}, perimeter {sums[0]} area {sums[1]}")
        total += sums[0] * sums[1]


for line in fields:
    output = ""
    for letter in line:
        output = f"{output}{letter["region"]}"
    print(output)


print(total)
