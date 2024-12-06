from aocd import get_data
from copy import deepcopy
import numpy
from dataclasses import dataclass

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

@dataclass
class Guard:
    X: int = 0
    Y: int = 0
    D: int = 0


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

positions = [(guardPos[0], guardPos[1], guardDir)]

def checkIfLoops(guardPos, guardDir, previousPositions):
    if (guardPos[0], guardPos[1], guardDir) in previousPositions:
        return True
    while True:
        guardPos, guardDir, _ = advanceGuardAndCount(guardPos, guardDir)
        if guardDir < 0:
            return False
        if (guardPos[0], guardPos[1], guardDir) in previousPositions:
            return True
        previousPositions.append((guardPos[0], guardPos[1], guardDir))

validBlocksPositions = []

while True:
    print(f"X: {guardPos[0]}, Y: {guardPos[1]}, D: {guardDir}")
    newGuardPos, newGuardDir, advanced = advanceGuardAndCount(guardPos, guardDir)
    if newGuardDir < 0:
        break
    if advanced and (newGuardPos[0], newGuardPos[1], 0) not in positions and (newGuardPos[0], newGuardPos[1], 1) not in positions and (newGuardPos[0], newGuardPos[1], 2) not in positions and (newGuardPos[0], newGuardPos[1], 3) not in positions:
        # pretend you did not advance, put an obstacle instead (only if you did not walk here already
        pretendDir = (guardDir + 1) % 4
        pretendPosition = (guardPos[0], guardPos[1], pretendDir)
        if pretendPosition in positions:
            if tuple(newGuardPos) not in validBlocksPositions:
                validBlocksPositions.append(tuple(newGuardPos))
            # loops
        else:
            map[newGuardPos[0]][newGuardPos[1]] = 1
            if checkIfLoops(guardPos, pretendDir, deepcopy(positions)):
                print(f"You can put a block in {newGuardPos}")
                if tuple(newGuardPos) not in validBlocksPositions:
                    validBlocksPositions.append(tuple(newGuardPos))
            map[newGuardPos[0]][newGuardPos[1]] = 0
    positions.append((newGuardPos[0], newGuardPos[1], newGuardDir))
    guardPos = newGuardPos
    guardDir = newGuardDir
        
    

print(len(validBlocksPositions))
