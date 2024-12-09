from aocd import get_data
from copy import deepcopy

data = get_data(year=2024, day=9)

testData = "2333133121414131402"
testData = data

files = {}
space = {}

fileID = 0
fsIndex = 0

# acquire data
for index, letter in enumerate(testData):
    number = int(letter)
    if index % 2 == 0:
        # file
        files[fileID] = {"start": fsIndex, "len": number}
        fsIndex += number
        fileID += 1
    else:
        # empty space
        space[fsIndex] = number
        fsIndex += number

print(files)
print(space)

# defragment
for key in reversed(sorted(files)):
    filePos = files[key]["start"]
    fileLen = files[key]["len"]
    # join spaces
    for spacePos, spaceLen in sorted(deepcopy(space).items()):
        if fileLen <= spaceLen and filePos > spacePos:
            print(f"Moving file ID {key} to {spacePos}")
            # make new space where old file was
            space[filePos] = fileLen
            # move
            files[key] = {"start": spacePos, "len": fileLen}
            # make new space if file does not fill up the old space completely
            if spaceLen > fileLen:
                space[spacePos + fileLen] = spaceLen - fileLen
            # delete old space
            del space[spacePos]
            # join spaces (max 1)
            for spacePos, spaceLen in sorted(space.items()):
                if spacePos + spaceLen in space:
                    print(f"Joining space {spacePos}, {spaceLen} with {spacePos + spaceLen}, {space[spacePos + spaceLen]}")
                    space[spacePos] = spaceLen + space[spacePos + spaceLen]
                    del space[spacePos + spaceLen]
                    break
            # join spaces (max 1)
            for spacePos, spaceLen in sorted(space.items()):
                if spacePos + spaceLen in space:
                    print(f"Joining space {spacePos}, {spaceLen} with {spacePos + spaceLen}, {space[spacePos + spaceLen]}")
                    space[spacePos] = spaceLen + space[spacePos + spaceLen]
                    del space[spacePos + spaceLen]
                    break

            break

# calculate checksum
checksum = 0

for key, value in files.items():
    for ind in range(value["start"], value["start"] + value["len"]):
        checksum += key * ind

print(files)
print(space)

print(checksum)
