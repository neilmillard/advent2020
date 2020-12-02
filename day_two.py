from re import split

from lib import get_lines_from_file


def get_passwords_from_file(filepath='day1.txt'):
    passwords = []
    file_lines = get_lines_from_file(filepath)
    for line in file_lines:
        try:
            validator, password = split(':', line)
        except ValueError:
            print('Cannot find : in ', line)
        entry = {'password': password, 'validator': validator}
        passwords.append(entry)
    return passwords


class Validator(object):
    def __init__(self, validator_string):
        my_range, letter = split(' ', validator_string)
        low, high = split('-', my_range)
        self.high = int(high)
        self.low = int(low)
        self.letter = letter


def validator_count(entry):
    # count how many of validator letter is in password
    validator = Validator(entry['validator'])
    found = entry['password'].count(validator.letter)
    if validator.low <= found <= validator.high:
        print(
            f'{validator.low}-{validator.high} {validator.letter} found {found} times in {entry["password"]}')
        return True
    return False


def validator_position(entry):
    # check position of letter based on low high
    found_low = False
    valid_high = False
    validator = Validator(entry['validator'])
    # is letter at position low
    # check first char is a space
    if entry['password'][0] != ' ':
        print('Space not found')
    if entry['password'][validator.low] == validator.letter:
        found_low = True
    # is letter NOT at position high
    if entry['password'][validator.high] == validator.letter:
        valid_high = True

    # Exactly one of these positions must contain the given letter
    if valid_high != found_low:
        # print(f'Found {validator.letter} at {validator.low}-{validator.high}: {entry["password"]}')
        return True

    return False


def day_two():
    passwords = get_passwords_from_file('day2.txt')
    # the passwords array is a dict,
    # Validator is a range 3-5 and a letter
    # 3-6 a
    # Password is a string
    # A password is valid if the letter in the validator appears a number of times, matching the range

    # count = 0
    # for entry in passwords:
    #     if validator_count(entry):
    #         count += 1
    # print(count)

    # 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    # 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    # 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

    # print(validator_position(
    #     {'password': ' ccccccccc', 'validator': '2-9 c'}
    # ))

    countf = 0
    for entry in passwords:
        if validator_position(entry):
            countf += 1
    print(countf)
