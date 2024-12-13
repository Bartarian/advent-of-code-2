from aocd import get_data
import numpy

data = get_data(year=2024, day=13)

testData = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

# data = testData

cases = []

for line in data.splitlines():
    if line.startswith("Button A"):
        aX, aY = line.strip("Button A: X+").split(", Y+")
        aX = int(aX)
        ay = int(aY)
    if line.startswith("Button B"):
        bX, bY = line.strip("Button B: X+").split(", Y+")
        bX = int(bX)
        by = int(bY)
    if line.startswith("Prize"):
        pX, pY = line.strip("Prize: X=").split(", Y=")
        pX = int(pX)
        py = int(pY)
        cases.append((numpy.array([[aX, bX], [aY, bY]], dtype=numpy.double), numpy.array([pX, pY], dtype=numpy.double)))

total = 0

for case in cases:
    solution = numpy.linalg.solve(case[0], case[1])
    if numpy.absolute(solution[0] - round(solution[0])) < 1e-12 and numpy.absolute(solution[1] - round(solution[1])) < 1e-12:
        total += solution[0] * 3 + solution[1]

print(total)
