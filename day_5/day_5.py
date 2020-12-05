def readentries(filename="input.txt"):
    with open(filename, "r") as filein:
        return [line.strip('\n') for line in filein]

def findRow(input):
    left = 0
    right = 127
    half = (right + 1)/2
    for i in range(7):
        if input[i] == "F":
            right -= half
        else:
            left += half
        half /= 2
    return left

def findColumn(input):
    left = 0
    right = 7
    half = (right + 1) / 2
    for i in range(3):
        if input[i+7] == "L":
            right -= half
        else:
            left += half
        half /= 2
    return left

def part1(entries):
    top = 0
    for input in entries:
        result = (findRow(input) * 8) + (findColumn(input))
        if result > top:
            top = result
    return top

def sorted_ids(entries):
    ids = []
    for input in entries:
        result = (findRow(input) * 8) + (findColumn(input))
        ids.append(result)
    ids.sort()
    return ids

def part2(sortedids):
    for i in range(len(sortedids)-1):
        if sortedids[i] + 1 != sortedids[i+1]:
            return sortedids[i+1] -1

def main():
    entries = readentries()
    print(part1(entries))
    ids = sorted_ids(entries)
    print(part2(ids))

main()

