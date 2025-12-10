DIAL_START = 50
DIAL_SIZE = 100


def get_direction(line: str) -> str:
    return line[0:1:]


def get_distance(line: str) -> int:
    return int(line[1::])


def turn_dial(start_position: int, direction: str, distance: int) -> int:
    if direction == 'R':
        return (start_position + distance) % DIAL_SIZE
    else:
        return (start_position - distance) % DIAL_SIZE


def main():
    with open('input.txt', encoding="utf-8") as f:
        zero_count = 0
        dial_position = DIAL_START
        for line in f:
            direction = get_direction(line)
            distance = get_distance(line)
            dial_position = turn_dial(dial_position, direction, distance)

            if dial_position == 0:
                zero_count += 1

        print(zero_count)


if __name__ == "__main__":
    main()
