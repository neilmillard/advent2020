from unittest import TestCase

from day7.main import get_rules, get_bag_data, part_a
from lib import get_lines_from_file


class TestBags(TestCase):
    def setUp(self) -> None:
        pass

    def test_get_bags(self):
        lines = get_lines_from_file('day7test.txt', True)
        rules = get_rules(lines)
        # rules = get_bag_data(lines)
        test_rules = {
            'light red': {'bright white': '1', 'muted yellow': '2'},
            'dark orange': {'bright white': '3', 'muted yellow': '4'},
            'bright white': {'shiny gold': '1'},
            'muted yellow': {'shiny gold': '2', 'faded blue': '9'},
            'shiny gold': {'dark olive': '1', 'vibrant plum': '2'},
            'dark olive': {'faded blue': '3', 'dotted black': '4'},
            'vibrant plum': {'faded blue': '5', 'dotted black': '6'},
            'faded blue': {},
            'dotted black': {}
        }
        self.assertEqual(rules, test_rules)

    def test_part_a(self):
        lines = get_lines_from_file('day7test.txt', True)
        rules = get_rules(lines)

        matches = part_a(rules)
        self.assertEqual(4, matches)
