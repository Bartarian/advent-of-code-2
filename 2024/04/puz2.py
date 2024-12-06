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

for lin in range(lines-2):
    for col in range(columns-2):
        if ((puzzle[lin][col] == 1 and puzzle[lin+1][col+1] == 2 and puzzle[lin+2][col+2] == 3) or (puzzle[lin][col] == 3 and puzzle[lin+1][col+1] == 2 and puzzle[lin+2][col+2] == 1)) and ((puzzle[lin+2][col] == 1 and puzzle[lin+1][col+1] == 2 and puzzle[lin][col+2] == 3) or (puzzle[lin+2][col] == 3 and puzzle[lin+1][col+1] == 2 and puzzle[lin][col+2] == 1)):
            print(f"Found match in {lin+1}, {col+1}")
            total += 1

print(total)
