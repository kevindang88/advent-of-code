import unittest
from day_02_part_2 import *


class TestDayTwo(unittest.TestCase):

    def test_parse_input(self):
        input = "11-22,95-115,998-1012,1188511880-1188511890\n"
        expected = ["11-22", "95-115", "998-1012", "1188511880-1188511890"]
        id_ranges = parse_input(input)
        self.assertEqual(id_ranges, expected)

    def test_parse_range(self):
        id_range = "95-115"
        expected = (95, 115)
        result = parse_range(id_range)
        self.assertEqual(result, expected)

    def test_generate_splits(self):
        test_cases = [
            ("12", [["1", "2"]]),
            ("1234", [["1", "2", "3", "4"], ["12", "34"]]),
            (
                "123456",
                [["1", "2", "3", "4", "5", "6"], ["12", "34", "56"], ["123", "456"]],
            ),
        ]
        for text, expected in test_cases:
            with self.subTest(text=text, expected=expected):
                self.assertEqual(list(generate_splits(text)), expected)

    def test_substrings_match(self):
        test_cases = [
            (["123", "123"], True),
            (["12", "31", "23"], False),
            (["1", "1", "1", "1"], True),
        ]
        for substrings, expected in test_cases:
            with self.subTest(substrings=substrings, expected=expected):
                self.assertEqual(substrings_match(substrings), expected)

    def test_id_is_invalid(self):
        test_cases = [
            (1, False),
            (11, True),
            (101, False),
            (123123, True),
            (1231234, False),
            (38593859, True),
        ]

        for input_str, expected in test_cases:
            with self.subTest(input=input_str, expected=expected):
                self.assertEqual(id_is_invalid(input_str), expected)

    def test_get_invalid_ids(self):
        test_cases = [
            (11, 22, [11, 22]),
            (95, 115, [99, 111]),
            (998, 1012, [999, 1010]),
        ]

        for start_id, end_id, expected in test_cases:
            with self.subTest(start_id=start_id, end_id=end_id, expected=expected):
                self.assertEqual(get_invalid_ids(start_id, end_id), expected)


if __name__ == "__main__":
    unittest.main()
