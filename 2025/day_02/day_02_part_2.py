def parse_input(input: str) -> list[str]:
    return input.strip().split(",")


def parse_range(id_range: str) -> tuple[int, int]:
    start, end = id_range.strip().split("-")
    return int(start), int(end)


def id_is_invalid(id: int) -> bool:
    splits = generate_splits(str(id))
    return any(substrings_match(split) for split in splits)


def generate_splits(s: str):
    """Generate all possible splits of string s into equal-length substrings."""
    length = len(s)
    for substring_length in range(1, length):
        if length % substring_length == 0:
            substrings = [
                s[i : i + substring_length] for i in range(0, length, substring_length)
            ]
            yield substrings


def substrings_match(substrings):
    return all(s == substrings[0] for s in substrings)


def get_invalid_ids(start_id: int, end_id: int):
    id_range = range(int(start_id), int(end_id) + 1)
    return list(filter(id_is_invalid, id_range))


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
