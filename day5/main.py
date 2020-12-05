import math

from lib import get_lines_from_file


# passports are k:v strings separated by a blank line
def tickets_from_file(filepath='input.txt'):
    tickets = []
    lines = get_lines_from_file(filepath, True)
    for line in lines:
        if line.strip():
            tickets.append(line.strip())

    return tickets


# binary space partitioning
def get_code(row_code, low='F', high='B'):
    _lower = 0
    _upper = 2 ** len(row_code) - 1
    for selector in row_code:
        diff = math.ceil((_upper - _lower) / 2)
        if selector == low:
            _upper -= diff
        if selector == high:
            _lower += diff
    return _upper


def find_seat_location(ticket):
    # we need a binary walk function to find the row.
    row = get_code(ticket[:7])
    column = get_code(ticket[7:10], 'L', 'R')
    return row, column


# Every seat also has a unique seat ID: multiply the row by 8, then add the column.
# In this example, the seat has ID 44 * 8 + 5 = 357.
def get_seat_id(row, column):
    return row * 8 + column


# create an array of seats, then fill with ticket holders
def fill_the_plane(tickets, row=127, column=7):
    plane = [[0 for i in range(column + 1)] for j in range(row + 1)]
    for ticket in tickets:
        seat_row, seat_col = find_seat_location(ticket)
        plane[seat_row][seat_col] = 1
    return plane


def find_empty_seats(plane):
    for row in range(len(plane)):
        for column in range(len(plane[row])):
            if plane[row][column] == 0:
                if 1 in plane[row]:
                    print(f'row:{row},col{column}: ID {get_seat_id(row, column)}')


def day_five():
    # seat = find_seat_location('FBFBBFFRLR')
    # print(seat)
    # print(get_seat_id(*seat))

    # step 1, find the highest ID in the input data.
    tickets = tickets_from_file('day5/input.txt')
    highest = 0
    for ticket in tickets:
        seat_id = get_seat_id(*find_seat_location(ticket))
        if seat_id > highest:
            highest = seat_id
    print(f'Highest seat ID: {highest}')

    plane = fill_the_plane(tickets, row=127, column=7)
    find_empty_seats(plane)
