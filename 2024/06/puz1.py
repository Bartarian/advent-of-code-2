from aocd import get_data
import numpy

data = get_data(year=2024, day=6)

testData = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

# allLines = testData.splitlines()
allLines = data.splitlines()

rows = len(allLines)
cols = len(allLines[0])

map = numpy.zeros(shape=(rows, cols), dtype=numpy.short)

guardPos = [-1, -1]
guardDir = -1

for lineNum, line in enumerate(allLines):
    for colNum, ch in enumerate(line):
        if ch == ".":
            continue
        elif ch == "#":
            map[lineNum][colNum] = 1
        elif ch == "^":
            guardPos = [lineNum, colNum]
            guardDir = 0
        elif ch == ">":
            guardPos = [lineNum, colNum]
            guardDir = 1
        elif ch == "v":
            guardPos = [lineNum, colNum]
            guardDir = 2
        elif ch == "<":
            guardPos = [lineNum, colNum]
            guardDir = 3

def advanceGuardAndCount(pos, dir):
    match dir:
        case 0:
            newPos = [pos[0] - 1, pos[1]]
        case 1:
            newPos = [pos[0], pos[1] + 1]
        case 2:
            newPos = [pos[0] + 1, pos[1]]
        case 3:
            newPos = [pos[0], pos[1] - 1]
        case _:
            raise ValueError(f"Invalid dir {dir}")

    if newPos[0] >= rows or newPos[0] < 0 or newPos[1] < 0 or newPos[1] >= cols:
        return newPos, -1, False

    if map[newPos[0]][newPos[1]] == 1:
        newDir = (dir + 1) % 4
        newPos = pos
        advanced = False
    else:
        newDir = dir
        advanced = True
    return newPos, newDir, advanced

print(tuple(guardPos))
positions = [(guardPos[0], guardPos[1])]

while True:
    guardPos, guardDir, advanced = advanceGuardAndCount(guardPos, guardDir)
    print(guardPos, advanced)
    if guardDir < 0:
        break
    if advanced:
        positions.append(tuple(guardPos))

print(len(set(positions)))
