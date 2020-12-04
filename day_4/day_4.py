# -- Vars. --
file_input = 'input.txt'
passports = []
counter = 0

# -- Open File --
with open(file_input, encoding='utf-8') as file:
    contents = file.read()
    inputs = contents.split('\n\n')

# -- List to Dict. --
for index, i in enumerate(inputs):
    data = i.replace('\n',' ').split()
    details = [i.split(':') for i in data]
    dict = {x[0]:x[1] for x in details}
    passports.append(dict)

# -- Validators --
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
fields.remove('cid')

def byr(x):
    return len(x) == 4 and int(x) >= 1920 and int(x) <= 2002

def iyr(x):
    return len(x) == 4 and int(x) >= 2010 and int(x) <= 2020

def eyr(x):
    return len(x) == 4 and int(x) >= 2020 and int(x) <= 2030

def hgt(x):
    if x[-2:] == 'cm':
        return int(x[:-2]) >= 150 and int(x[:-2]) <= 193
    elif x[-2:] == 'in':
        return int(x[:-2]) >= 59 and int(x[:-2]) <= 76

def hcl(x):
    return x[0] == '#' and len(x[1:]) == 6 and x[1:].isalnum()

def ecl(x):
    return x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def pid(x):
    return len(x) == 9


for index, x in enumerate(passports):
    keys = x.keys()
    if all(field in keys for field in fields):
        if all([byr(x['byr']), iyr(x['iyr']), eyr(x['eyr']), hgt(x['hgt']), hcl(x['hcl']), ecl(x['ecl']), pid(x['pid'])]):
            counter += 1

print(counter)