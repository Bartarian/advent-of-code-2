from aocd import get_data

import re

data = get_data(year=2024, day=3)

testData = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

total = 0

pattern = r"mul\((\d*),(\d*)\)"

#matches = re.findall(pattern, testData)
matches = re.findall(pattern, data)

for i in matches:
    total += int(i[0]) * int(i[1])

print(total)
