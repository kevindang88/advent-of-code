with open('input.txt', encoding="utf-8") as f:
    zero_count = 0
    dial_start = 50
    dial_position = dial_start
    for line in f:
        direction = line[0:1:]
        distance = int(line[1::])
        sign = 1 if direction == 'R' else -1
        dial_position = (dial_position + (sign * distance)) % 100

        if dial_position == 0:
            zero_count += 1

    print(zero_count)
