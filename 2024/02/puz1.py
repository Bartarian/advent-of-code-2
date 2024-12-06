from aocd import get_data

data = get_data(year=2024, day=2)

testData = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
13 16 15 13 10 6
1 3 6 7 9"""

total = 0

for line in data.splitlines():
    _break = False
    numbers = [int(x) for x in line.strip("\n").split(" ")]
    if numbers[1] == numbers[0]:
        # equals = unsafe
        continue
    elif numbers[1] > numbers[0]:
        # ascending
        for i, num in enumerate(numbers[:-1]):
            if _break:
                break
            if num >= numbers[i+1] or numbers[i+1]-num > 3:
                # unsafe
                _break = True
    else:
        # descending
        for i, num in enumerate(numbers[:-1]):
            if _break:
                break
            if num <= numbers[i+1] or num-numbers[i+1] > 3:
                # unsafe
                _break = True
    if _break:
        continue
    total+=1
    print(line)

print(total)

