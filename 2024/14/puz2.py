from aocd import get_data
from time import sleep
import os

data = get_data(year=2024, day=14)

rows = 103
cols = 101

testData = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

testRows = 7
testCols = 11

test = not True

if test:
    data = testData
    rows = testRows
    cols = testCols

robots = []

for line in data.splitlines():
    p, v = line.split(" ")
    posX, posY = p.strip("p=").split(",")
    velX, velY = v.strip("v=").split(",")
    robot = {"Pos X": int(posX), "Pos Y": int(posY), "Vel X": int(velX), "Vel Y": int(velY)}
    robots.append(robot)

seconds = 7406

quadZero = 0
quadOne = 0
quadTwo = 0
quadThree = 0

while True:
    seconds += 1
    positions = []
    for robot in robots:
        posX = (seconds * robot["Vel X"] + robot["Pos X"]) % cols
        posY = (seconds * robot["Vel Y"] + robot["Pos Y"]) % rows
        if posX < cols // 2:
            if posY < rows // 2:
                quadZero += 1
        if posX > cols // 2:
            if posY < rows // 2:
                quadOne += 1
        if posX > cols // 2:
            if posY > rows // 2:
                quadTwo += 1
        if posX < cols // 2:
            if posY > rows // 2:
                quadThree += 1
        positions.append((posX, posY))
    for rowInd in range(rows):
        row = ""
        for colInd in range(rows):
            if (colInd, rowInd) in positions:
                row = f"{row}X"
            else:
                row = f"{row} "
        print(row)

    print(seconds)
    input()

