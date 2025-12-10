START_POSITION = 50
DIAL_SIZE = 100


def get_direction(line: str) -> str:
    return line[0:1:]


def get_distance(line: str) -> int:
    return int(line[1::])


def turn_dial(start_position: int, direction: str, distance: int) -> int:
    if direction == "R":
        return (start_position + distance) % DIAL_SIZE
    else:
        return (start_position - distance) % DIAL_SIZE


def get_distance_to_zero(direction: str, dial_position: int) -> int:
    if dial_position == 0:
        return DIAL_SIZE
    if direction == "R":
        return DIAL_SIZE - dial_position
    else:
        return dial_position


def count_clicks_on_zero(distance: int, distance_to_zero: int) -> int:
    if distance >= distance_to_zero:
        return 1 + int((distance - distance_to_zero) / DIAL_SIZE)
    return 0


def main():
    with open("input.txt", encoding="utf-8") as f:
        zero_count = 0
        dial_position = START_POSITION
        for line in f:
            direction = get_direction(line)
            distance = get_distance(line)

            distance_to_zero = get_distance_to_zero(direction, dial_position)
            zero_count += count_clicks_on_zero(distance, distance_to_zero)

            dial_position = turn_dial(dial_position, direction, distance)

        print("zero count:", zero_count)


if __name__ == "__main__":
    main()
