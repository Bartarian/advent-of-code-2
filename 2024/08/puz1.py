from aocd import get_data
from dataclasses import dataclass
from itertools import permutations, combinations
import numpy

data = get_data(year=2024, day=8)

testData = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

# allLines = testData.splitlines()
allLines = data.splitlines()

lines = len(allLines)
cols = len(allLines[0])

antennas = {}

for lineN, line in enumerate(allLines):
    for lettN, letter in enumerate(line):
        if letter != ".":
            if letter in antennas:
                antennas[letter].append((lineN, lettN))
            else:
                antennas[letter] = [(lineN, lettN)]

def inBoundaries(point: tuple[int, int]) -> bool:
    if 0 <= point[0] < lines and 0 <= point[1] < cols:
        return True
    return False

allAntinodes = []

for antenna, positions in antennas.items():
    print("******")
    print(f"Antenna: {antenna}")
    for pair in combinations(positions, 2):
    # for pair in permutations(positions, 2):
        print(pair)
        antinodes = ((2 * pair[0][0] - pair[1][0], 2 * pair[0][1] - pair[1][1]), (2 * pair[1][0] - pair[0][0], 2 * pair[1][1] - pair[0][1]))
        for candidate in antinodes:
            if inBoundaries(candidate):
                allAntinodes.append(candidate)

print("******")

print(len(set(allAntinodes)))

