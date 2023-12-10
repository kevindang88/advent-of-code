import re

sum = 0

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


with open("input") as file:
    for line in file:
        left_digit = re.search("\\d|" + "|".join(numbers.keys()), line).group()
        right_digit = re.search(
            "\\d|" + "|".join(numbers.keys())[::-1], line[::-1]
        ).group()[::-1]
        calibration_value = "".join(
            map(
                lambda x: x if x.isdigit() else numbers.get(x),
                [left_digit, right_digit],
            )
        )
        sum = sum + int(calibration_value)

        print(calibration_value)

print(sum)
