from unittest import TestCase

import pytest

from day5.main import find_seat_location, get_seat_id


test_data = [
        {'ticket': 'FBFBBFFRLR',
         'row': 44,
         'column': 5,
         'id': 357
         },
        {'ticket': 'BFFFBBFRRR',
         'row': 70,
         'column': 7,
         'id': 567
         },
        {'ticket': 'FFFBBBFRRR',
         'row': 14,
         'column': 7,
         'id': 119
         },
        {'ticket': 'BBFFBBFRLL',
         'row': 102,
         'column': 4,
         'id': 820
         }
    ]


class TestSeat(TestCase):
    def test_find_seat_location(self):
        for data in test_data:
            result = find_seat_location(data['ticket'])
            self.assertEqual(data['row'], result[0])
            self.assertEqual(data['column'], result[1])

    def test_get_id(self):
        for data in test_data:
            self.assertEqual(data['id'], get_seat_id(data['row'], data['column']))
