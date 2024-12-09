from aocd import get_data

data = get_data(year=2024, day=9)

testData = "2333133121414131402"
testData = "132"
testData = data

fs = []

content = 0

for index, letter in enumerate(testData):
    number = int(letter)
    if index % 2 == 0:
        # file
        for fileInd in range(number):
            fs.append(content)
        content += 1
    else:
        for spaceInd in range(number):
            fs.append(-1)

start = 0
end = len(fs)

for ind, file in reversed(list(enumerate(fs))):
    if file == -1:
        continue
    if ind <= start:
        break
    # print(f"moving file id {file}, to somewhere between {start} end {end}")
    for targetInd in range(start, end):
        if fs[targetInd] == -1:
            fs[targetInd] = file
            fs[ind] = -1
            start = targetInd + 1
            end = ind
            break
    # print(start, end)
    # print(fs)
    if start >= end:
        break

total = 0

counter = 0
while fs[counter] >=0:
    total += counter * fs[counter]
    counter += 1

print(fs)
print(total)
