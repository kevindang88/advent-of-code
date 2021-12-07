import re

with open('day_05/input_05.txt') as input:
    coords = {}
    for line in input:
        x1, y1, x2, y2 = [int(i) for i in re.split(',| -> ', line)]
        if x1 == x2 or y1 == y2:
            for i in range(abs(x1 - x2) + 1):
                for j in range(abs(y1 - y2) + 1):
                    c = (min(x1, x2) + i, min(y1, y2) + j)
                    if c not in coords:
                        coords[c] = 1
                    else:
                        coords[c] += 1

    overlaps = sum(x > 1 for x in coords.values())
    print(overlaps)
