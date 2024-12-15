from aocd import get_data

data = get_data(year=2024, day=15)

testData = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

testData2 = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

# data = testData2

fullMap = []
moves = []

movesTranslation = {"^": 0, ">": 1, "v": 2, "<": 3}

inMap = True
for lineNum, line in enumerate(data.splitlines()):
    if inMap:
        if line == "":
            inMap = False
        else:
            fullMap.append([])
            for letterNum, letter in enumerate(line):
                if letter == "#":
                    fullMap[lineNum].append(0)
                elif letter == ".":
                    fullMap[lineNum].append(1)
                elif letter == "O":
                    fullMap[lineNum].append(2)
                else:
                    fullMap[lineNum].append(1)
                    robotPosition=(lineNum, letterNum)
    else:
        for element in line:
            moves.append(movesTranslation[element])

print(fullMap)
assert(robotPosition)
print(robotPosition)
print(moves)


columns = len(fullMap[0])
rows = len(fullMap)


def prettyPrinter():
    output = ""
    for line in fullMap:
        for letter in line:
            if letter == 0:
                output = f"{output}#"
            elif letter == 1:
                output = f"{output}."
            elif letter == 2:
                output = f"{output}O"
        output = f"{output}\n"
    print(output)


def moveAndPush(row, col, dir):
    if fullMap[row][col] == 0:
        # Trying to move a wall
        print("trying to move a wall")
        return None
    else:
        item = fullMap[row][col]
        match dir:
            case 0:
                destination = (row - 1, col)
            case 1:
                destination = (row, col + 1)
            case 2:
                destination = (row + 1, col)
            case 3:
                destination = (row, col - 1)
            case _:
                raise ValueError(f"can't move if casse is {dir}")
        if (destination[0] < 0) or (destination[0] >= rows) or (destination[1] < 0) or (destination[1] >= columns):
            # prob no need
            print("out of map. Weird, there should be walls")
            return None
        if fullMap[destination[0]][destination[1]] == 0:
            # can't move into walls
            print("trying to move in a wall")
            return None
        elif fullMap[destination[0]][destination[1]] == 1:
            # successful move to empy space
            fullMap[destination[0]][destination[1]] = item
            fullMap[row][col] = 1
            return destination
        elif fullMap[destination[0]][destination[1]] == 2:
            # Box, try to move it
            if moveAndPush(destination[0], destination[1], dir):
                # it worked
                fullMap[destination[0]][destination[1]] = item
                fullMap[row][col] = 1
                return destination
            else:
                return None

for move in moves:
    print(f"moving {robotPosition} in dir {move}")
    result = moveAndPush(robotPosition[0], robotPosition[1], move)
    print(f"move result was {result}")
    prettyPrinter()
    if result:
        robotPosition = result
    
prettyPrinter()

score = 0

for lineNum, line in enumerate(fullMap):
    for letterNum, letter in enumerate(line):
        if letter == 2:
            score += 100 * lineNum + letterNum

print(score)
