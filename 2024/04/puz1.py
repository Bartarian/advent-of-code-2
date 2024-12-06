from aocd import get_data
import numpy
import re

data = get_data(year=2024, day=4)

testData = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

lines = 0
columns = 0

# allLines = testData.splitlines()
allLines = data.splitlines()

for line in allLines:
    if not columns:
        for letter in line:
            if letter in ["X", "M", "A", "S"]:
                columns += 1
    lines += 1

puzzle = numpy.zeros(shape=(lines, columns), dtype=numpy.short)

for line in range(lines):
    for col in range(columns):
        letter = allLines[line][col]
        number = -1
        match letter:
            case "X":
                number = 0
            case "M":
                number = 1
            case "A":
                number = 2
            case "S":
                number = 3

        puzzle[line][col] = number

total = 0

# Horizontal
for line in range(lines):
    for col in range(columns - 3):
        if (puzzle[line][col] == 0 and puzzle[line][col+1] == 1 and puzzle[line][col+2] == 2 and puzzle[line][col+3] == 3) or (puzzle[line][col] == 3 and puzzle[line][col+1] == 2 and puzzle[line][col+2] == 1 and puzzle[line][col+3] == 0):
            print(f"Found horizontal match in {line} {col}")
            total += 1

# Vertical
for line in range(lines - 3):
    for col in range(columns):
        if (puzzle[line][col] == 0 and puzzle[line+1][col] == 1 and puzzle[line+2][col] == 2 and puzzle[line+3][col] == 3) or (puzzle[line][col] == 3 and puzzle[line+1][col] == 2 and puzzle[line+2][col] == 1 and puzzle[line+3][col] == 0):
            print(f"Found vertical match in {line} {col}")
            total += 1

# direction \
for line in range(lines - 3):
    for col in range(columns -3):
        if (puzzle[line][col] == 0 and puzzle[line+1][col+1] == 1 and puzzle[line+2][col+2] == 2 and puzzle[line+3][col+3] == 3) or (puzzle[line][col] == 3 and puzzle[line+1][col+1] == 2 and puzzle[line+2][col+2] == 1 and puzzle[line+3][col+3] == 0):
            print(f"Found \\ match in {line} {col}")
            total += 1

# direction /
for line in range(lines - 3):
    for col in range(columns -3):
        if (puzzle[line+3][col] == 0 and puzzle[line+2][col+1] == 1 and puzzle[line+1][col+2] == 2 and puzzle[line][col+3] == 3) or (puzzle[line+3][col] == 3 and puzzle[line+2][col+1] == 2 and puzzle[line+1][col+2] == 1 and puzzle[line][col+3] == 0):
            print(f"Found / match in {line+3} {col}")
            total += 1

print(total)
