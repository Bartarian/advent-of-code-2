from aocd import data

left = []
right = []

for line in data.splitlines():
    if line:
        a, b = line.split("   ")
        left.append(a)
        right.append(b)

left.sort()
right.sort()

print(left)
print(right)


total = 0

for index, item in enumerate(left):
    a = int(item)
    b = int(right[index])
    print(f"{b} - {a} = {b - a}")
    total += abs(b - a)

print(total)
