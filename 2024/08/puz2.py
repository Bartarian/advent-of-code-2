from aocd import get_data
from itertools import combinations
from math import gcd

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
        deltaL = pair[0][0] - pair[1][0]
        deltaC = pair[0][1] - pair[1][1]
        if deltaL == 0:
            antinodes = [(lin, pair[0][1]) for lin in range(lines)]
        elif deltaC == 0:
            antinodes = [(pair[0][0], col) for col in range(cols)]
        else:
            myGcd = gcd(deltaL, deltaC)
            deltaL = deltaL // myGcd
            deltaC = deltaC // myGcd
            # start with the antenna themselves
            antinodes = [pair[0], pair[1]]
            for i in range(lines):
                # overkill
                antinodes.append((pair[0][0] + i * deltaL, pair[0][1] + i * deltaC))
                antinodes.append((pair[0][0] - i * deltaL, pair[0][1] - i * deltaC))
        for candidate in antinodes:
            if inBoundaries(candidate) and candidate not in allAntinodes:
                print(f"Adding {candidate}")
                allAntinodes.append(candidate)

print("******")

print(len(set(allAntinodes)))

