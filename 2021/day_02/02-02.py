with open('day_02/input_02.txt') as input:
    horiz, depth, aim = 0, 0, 0
    for line in input:
        direction, value = line.split()
        match direction:
            case 'forward':
                horiz += int(value)
                depth += aim * int(value)
            case 'down':
                aim += int(value)
            case 'up':
                aim -= int(value)
    print(horiz * depth)