from aocd import get_data

import re

data = get_data(year=2024, day=3)

testData = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# data = testData

total = 0

badPattern = r"don't\(\)[\S\n\t\v ]*?do\(\)"
badPatternCleanup = r"don't\(\)[\S\n\t\v ]*"

goodPattern = r"mul\((\d*),(\d*)\)"

prePreProcessedData = re.sub(badPattern, "", data)
preProcessedData = re.sub(badPatternCleanup, "", prePreProcessedData)

matches = re.findall(goodPattern, preProcessedData)

for i in matches:
    total += int(i[0]) * int(i[1])

print(total)
