with open('day_02/input_02.txt') as input:
    horiz, depth = 0, 0
    for line in input:
        direction, value = line.split()
        match direction:
            case 'forward':
                horiz += int(value)
            case 'down':
                depth += int(value)
            case 'up':
                depth -= int(value)
    print(horiz * depth)
