import re

symbol_pattern = r"[^\w\.]"


def get_sides(line):
    return re.findall(str.format(r"\d+(?={0})|(?<={0})\d+", symbol_pattern), line)


def main():
    with open("2023/03/input.txt") as file:
        lines = list(file)
        for line in lines:
            print(get_sides(line))


main()
