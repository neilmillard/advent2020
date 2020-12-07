from unittest import TestCase

from day6.main import get_yes_from_group, add_results, get_dupe_yes_from_group


class TestSeat(TestCase):
    def setUp(self) -> None:
        self.groups1 = [
            ['abc'],
            ['a', 'b', 'c'],
            ['ab', 'ac'],
            ['a', 'a', 'a', 'a'],
            ['b']
        ]
        self.answers1 = [3, 3, 3, 1, 1]
        self.dupe_answers = [3, 0, 1, 1, 1]
        self.groups2 = [
            ['sgqytjiw', 'gkwqybtims']
        ]
        self.answers2 = [11]
        self.dupe_answers2 = [7]

    def test_get_yes_from_group(self):
        result = get_yes_from_group(self.groups1)
        self.assertEqual(len(self.answers1), len(result))
        self.assertEqual(self.answers1, result)

        result = get_yes_from_group(self.groups2)
        self.assertEqual(len(self.answers2), len(result))
        self.assertEqual(self.answers2, result)

    def test_get_dupe_yes_from_group(self):
        result = get_dupe_yes_from_group(self.groups1)
        self.assertEqual(len(self.dupe_answers), len(result))
        self.assertEqual(self.dupe_answers, result)

        result = get_dupe_yes_from_group(self.groups2)
        self.assertEqual(len(self.dupe_answers2), len(result))
        self.assertEqual(self.dupe_answers2, result)

    def test_add_results(self):
        sum = add_results(self.answers1)
        self.assertEqual(11, sum)
        sum2 = add_results(self.dupe_answers)
        self.assertEqual(6, sum2)
