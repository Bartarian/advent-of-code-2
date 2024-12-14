from aocd import get_data
import sympy

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
        pX = int(pX) + 10000000000000
        pY = int(pY) + 10000000000000
        cases.append((sympy.Matrix([[aX, bX], [aY, bY]]), sympy.Matrix([pX, pY])))

total = int(0)

for case in cases:
    solution = case[0].inv() * case[1]
    if isinstance(solution[0], sympy.core.numbers.Integer) and isinstance(solution[1], sympy.core.numbers.Integer):
        total += solution[0] * 3 + solution[1]

print(total)
