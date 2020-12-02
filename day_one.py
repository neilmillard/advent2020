from lib import get_lines_from_file


def get_numbers_from_file(filepath='day1.txt'):
    numbers = []
    file_lines = get_lines_from_file(filepath)
    for line in file_lines:
        numbers.append(int(line))
    return numbers


def find_pairs(number_list):
    target = 2020
    for number_one in number_list:
        for number_two in number_list:
            for number_three in number_list:
                if number_three + number_two + number_one == target:
                    print(f'Found: {number_one} + {number_two} + {number_three} = {target}')
                    answer = number_two * number_one * number_three
                    print(f'Answer: {answer}')


def day_one():
    my_numbers = get_numbers_from_file()
    find_pairs(my_numbers)
