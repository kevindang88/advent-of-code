import unittest
from day_01_part_2 import *


class TestDayOne(unittest.TestCase):

    def tearDown(self):
        pass

    def test_parse_direction(self):
        input = ["L5\n", "R13\n", "L456\n", "R1234\n"]
        result = list(map(get_direction, input))
        self.assertEqual(result, ["L", "R", "L", "R"])

    def test_parse_distance(self):
        input = ["L5\n", "R13\n", "L456\n", "R1234\n"]
        result = list(map(get_distance, input))
        self.assertEqual(result, [5, 13, 456, 1234])

    def test_turn_dial(self):
        test_cases = [
            (50, "R10\n", 60, "simple right turn"),
            (50, "L20\n", 30, "simple left turn"),
            (90, "R10\n", 0, "right turn lands on zero"),
            (5, "L5\n", 0, "left turn lands on zero"),
            (75, "R30\n", 5, "right turn passes zero once"),
            (25, "L26\n", 99, "left turn passes zero once"),
            (45, "R201\n", 46, "right turn passes zero twice"),
            (5, "L201\n", 4, "left turn passes zero twice"),
        ]
        for start_position, input_line, expected, description in test_cases:
            with self.subTest(
                start_position=start_position,
                input_line=input_line,
                expected=expected,
                msg=description,
            ):
                direction = get_direction(input_line)
                distance = get_distance(input_line)
                result = turn_dial(start_position, direction, distance)
                self.assertEqual(result, expected)

    def test_distance_to_zero(self):
        test_cases = [
            ("right turn from zero", 0, "R5", 100),
            ("right turn", 5, "R12", 95),
            ("left turn from zero", 0, "L5", 100),
            ("left turn", 5, "L20", 5),
        ]

        for description, start_position, input_line, expected_dtz in test_cases:
            with self.subTest(
                msg=description,
                start_position=start_position,
                input_line=input_line,
                expected_dtz=expected_dtz,
            ):
                direction = get_direction(input_line)
                distance = get_distance(input_line)
                result = get_distance_to_zero(direction, start_position)
                self.assertEqual(result, expected_dtz)

    def test_count_clicks_on_zero(self):
        test_cases = [
            ("right turn does not touch zero", 50, "R49\n", 0),
            ("right turn from zero", 0, "R5\n", 0),
            ("right turn lands on zero", 90, "R10\n", 1),
            ("right turn passes zero once", 90, "R11\n", 1),
            ("right turn passes zero twice", 50, "R201", 2),
            ("left turn does not touch zero", 5, "L4\n", 0),
            ("left turn from zero", 0, "L5", 0),
            ("left turn lands on zero", 5, "L5\n", 1),
            ("left turn passes zero once", 5, "L6\n", 1),
            ("left turn passes zero twice", 50, "L200\n", 2),
        ]

        for description, start_position, input_line, expected_count in test_cases:
            with self.subTest(
                start_position=start_position,
                input_line=input_line,
                expected_count=expected_count,
                msg=description,
            ):
                direction = get_direction(input_line)
                distance = get_distance(input_line)
                distance_to_zero = get_distance_to_zero(direction, start_position)
                result = count_clicks_on_zero(distance, distance_to_zero)
                self.assertEqual(result, expected_count)


if __name__ == "__main__":
    unittest.main()
