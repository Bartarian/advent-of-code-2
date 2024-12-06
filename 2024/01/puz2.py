from aocd import get_data
from collections import Counter

input = get_data(day=1, year=2024)
left = []
right = []

for line in input.splitlines():
    if line:
        a, b = line.split("   ")
        left.append(int(a))
        right.append(int(b))

rightCounted = Counter(right)

total = 0

for item in left:
    if item in rightCounted:
        total += item * rightCounted[item]

print(total)
