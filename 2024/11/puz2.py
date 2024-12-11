from aocd import get_data
from functools import cache

data = get_data(year=2024, day=11)


testData = '125 17'
# data = testData

stones = [int(x) for x in data.split(' ')]

@cache
def multiplyStone(number, blinks):
    if blinks == 1:
        if number == 0:
            return 1
        elif len(str(number)) % 2 == 0:
            return 2
        else:
            return 1
    else:
        if number == 0:
            return multiplyStone(1, blinks - 1)
        digits = str(number)
        if len(digits) % 2 == 0:
            left = int(digits[:len(digits) // 2])
            right = int(digits[len(digits) // 2:])
            return multiplyStone(left, blinks - 1) + multiplyStone(right, blinks - 1)
        else:
            return multiplyStone(number * 2024, blinks - 1)

total = 0

for stone in stones:
    total += multiplyStone(stone, 75)

print(total)
