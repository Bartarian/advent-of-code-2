from aocd import get_data

data = get_data(year=2024, day=11)


testData = '125 17'
data = testData

stones = [int(x) for x in data.split(' ')]


for blink in range(25):
    for index in range(len(stones) -1, -1, -1):
        if stones[index] == 0:
            stones[index] = 1
        else:
            digits = str(stones[index])
            if len(digits) % 2 == 0:
                left = int(digits[:len(digits) // 2])
                right = int(digits[len(digits) // 2:])
                stones[index] = right
                stones.insert(index, left)
            else:
                stones[index] *= 2024



print(len(stones))
