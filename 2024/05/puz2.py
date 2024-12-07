from aocd import get_data

data = get_data(year=2024, day=5)

testData = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

allLines = testData.splitlines()
# allLines = data.splitlines()

inRules = True

rules = []
pagesList = []
total = 0

for line in allLines:
    line = line.strip("\n")
    if line == "":
        inRules = False
        continue
    if inRules:
        leftN, rightN = line.split("|")
        newRule = (int(leftN), int(rightN))
        rules.append(newRule)
    else:
        numbers = line.split(",")
        pagesList.append(tuple([int(x) for x in numbers]))

# print(rules)
# print(pagesList)

brokenPages = []

for pages in pagesList:
    broken = False
    for pageIndex, page in enumerate(pages):
        if broken:
            break
        for rule in rules:
            if broken:
                break
            if page == rule[0]:
                # Matching rule for current page
                if (rule[1] in pages) and (pageIndex > pages.index(rule[1])):
                    print(f"Line {pages} breaks rule {rule}")
                    broken = True
                    brokenPages.append(pages)
    if not broken:
        print(f"Pages {pages} are valid")
        middlePage = pages[len(pages) // 2]
        total += middlePage

print(total)

total = 0

print("Starting reorder\n**************")

for pages in brokenPages:
    ordered = False
    workingPages = list(pages)
    while not ordered:
        restart = False
        for pageIndex, page in enumerate(workingPages):
            for rule in rules:
                if page == rule[0]:
                    if rule[1] in workingPages and pageIndex > workingPages.index(rule[1]):
                        # swap
                        print(workingPages)
                        workingPages[pageIndex] = rule[1]
                        workingPages[workingPages.index(rule[1])] = page
                        restart = True
                if restart:
                    break
            if restart:
                break
        if restart:
            continue
        ordered = True
        print(workingPages)
        print("***************")
        middlePage = workingPages[len(workingPages) // 2]
        total += middlePage

print(total)
