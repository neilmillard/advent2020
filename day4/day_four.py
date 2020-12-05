from lib import get_lines_from_file


# passports are k:v strings separated by a blank line
def passports_from_file(filepath='day4.txt'):
    passports = []
    lines = get_lines_from_file(filepath, True)
    entry = {}
    for line in lines:
        if line.strip():
            # split default is a ' '
            for kv in line.split():
                if ':' in kv:
                    k, v = kv.split(':')
                    entry[k] = v
        else:
            passports.append(entry)
            entry = {}

    return passports


def passport_complete(passport, required_fields):
    return all(f in passport for f in required_fields)


def passport_complete2(passport, required_fields):
    for field in required_fields:
        if field not in passport.keys():
            return False
    return True


def is_passport_valid(passport):
    for field_data in passport.items():
        if is_valid(*field_data) is False:
            return False
    return True


def is_valid(field, data):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if field == 'byr':
        if 1920 <= int(data) <= 2002:
            return True
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if field == 'iyr':
        if 2010 <= int(data) <= 2020:
            return True
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if field == 'eyr':
        if 2020 <= int(data) <= 2030:
            return True
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    if field == 'hgt':
        if data[-2:] == 'cm':
            if 150 <= int(data[0:-2]) <= 193:
                return True
        if data[-2:] == 'in':
            if 59 <= int(data[0:-2]) <= 76:
                return True
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if field == 'ecl':
        if data in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if field == 'hcl':
        if data[0] == '#' and len(data) == 7:
            for char in data[1:]:
                if char not in '0123456789abcdef':
                    return False
            return True
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if field == 'pid':
        if data.isdigit() and len(data) == 9:
            return True
    # cid (Country ID) - ignored, missing or not.
    if field == 'cid':
        return True
    return False


def count_valid(passports):
    # we have valid fields
    # required_fields = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'}
    required_fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    count = 0
    for passport in passports:
        # if is_valid(passport, required_fields):
        if passport_complete(passport, required_fields) and is_passport_valid(passport):
            count += 1
    return count


def day_four():
    passports = passports_from_file('day4/day4.txt')
    # check that required fields are present
    count = count_valid(passports)
    total = len(passports)
    print(f'{count}/{total}')
