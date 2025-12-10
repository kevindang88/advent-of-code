def parse_input(input: str) -> list[str]:
    return input.strip().split(",")


def parse_range(id_range: str) -> tuple[int, int]:
    start, end = id_range.strip().split("-")
    return int(start), int(end)


def is_invalid(id: int) -> bool:
    id_str = str(id)
    mid = int(len(str(id)) / 2)
    first_half = id_str[:mid]
    second_half = id_str[mid:]
    return first_half == second_half


def get_invalid_ids(start_id: int, end_id: int):
    id_range = range(int(start_id), int(end_id) + 1)
    return list(filter(is_invalid, id_range))


def main():
    with open("input", encoding="utf-8") as f:
        id_ranges = parse_input(f.read())
        invalid_id_sum = 0

        for id_range in id_ranges:
            start_id, end_id = parse_range(id_range)
            invalid_ids = get_invalid_ids(start_id, end_id)
            sum_in_range = sum(invalid_ids)
            invalid_id_sum += sum_in_range

        print("invalid_id_sum", invalid_id_sum)


if __name__ == "__main__":
    main()
