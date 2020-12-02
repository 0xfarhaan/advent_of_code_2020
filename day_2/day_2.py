def readentries(filename="input.txt"):
    with open(filename, "r") as filein:
        return [line.strip('\n') for line in filein]

def cleandata(entries):
    elements = []
    output = []
    for string in entries:
        temp = string.split(" ")
        elements.append(temp)

    for element in elements:
        minmaxstringarray = element[0].split("-")
        minmaxintarray = [int(x) for x in minmaxstringarray]
        hash = {}
        hash["min"] = minmaxintarray[0]
        hash["max"] = minmaxintarray[1]
        hash["letter"] = element[1][0]
        hash["password"] = element[2]
        output.append(hash)

    return output

def checkPassword(entry):
    charcount = entry["password"].count(entry["letter"])
    if charcount >= entry["min"] and charcount <= entry["max"]:
        return 1
    else:
        return 0

def part1(cleaneddata):
    count = 0
    for passworddata in cleaneddata:
        count += checkPassword(passworddata)

    return count

def part2(cleaneddata):
    count = 0
    for data in cleaneddata:
        if (data["password"][data["min"]-1] == data["letter"]) != (data["password"][data["max"]-1] == data["letter"]):
            count += 1
    return count


def main():
    entries = readentries()
    cleanentries = cleandata(entries)
    count = part1(cleanentries)
    print(count)
    part2count = part2(cleanentries)
    print(part2count)

main()