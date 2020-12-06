def readentries(filename="input.txt"):
    with open(filename, "r") as filein:
        return [line.strip('\n') for line in filein]

def cleandata(entries):
    data = []
    currentEntry = ''
    count = 0
    for entry in entries:
        if entry != '':
            currentEntry += entry
        else:
            data.append(currentEntry)
            currentEntry = ''
    data.append(currentEntry)

    return data

def part1(data):
    count = 0
    for group in data:
        count += len(set(group))

    return count

def part2(data):
    input = open("input.txt", "r")
    total = 0
    data = ''
    for line in input:
        if len(line) > 1:
            data += line.strip() + ' '
        else:
            data += line
    data = data.split('\n')
    for record in data:
        record = sorted(record.split(), key=len)
        total += sum(1 for i in record[0] if all(i in j for j in record))

    return total

def main():
    data = cleandata(readentries())
    print(part1(data))
    print(part2(data))

main()