#how to answer this question
#Read in the file and have each line be added as a string in an array
#For each string apply the +3 to get the new index position and then check that index of the next array
#If that index of the next array has a tree count it otherwise reapply the algorithm till you have traversed all the strings

def readentries(filename="input.txt"):
    with open(filename, "r") as filein:
        return [line.strip('\n') for line in filein]

def buildMap(entries, right, down):
    length = right*down
    grid = list(map(lambda x: x*length, entries))
    return grid

def countTrees(grid, right, down):
    count = 0
    column = 0
    row = 0

    while row + 1 < len(grid):
        row += down
        column += right

        if grid[row][column % len(grid[row])] == '#':
            count += 1

    return count

def countmultipleslopes(slopes, grid):
    multiplicationtotal = 1
    for slope in slopes:
        multiplicationtotal *= countTrees(grid, slope[0], slope[1])

    return multiplicationtotal

def main():
    entries = readentries()
    map = buildMap(entries,3,1)
    count = countTrees(map, 3, 1)
    print(count)
    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    print(countmultipleslopes(slopes, map))

main()