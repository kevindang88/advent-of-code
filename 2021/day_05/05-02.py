import re

with open('day_05/input_05.txt') as input:
    coords = {}

    def save_coords(c):
        if c not in coords:
            coords[c] = 1
        else:
            coords[c] += 1

    for line in input:
        x1, y1, x2, y2 = [int(i) for i in re.split(',| -> ', line)]
        if x1 == x2 or y1 == y2:
            for i in range(abs(x1 - x2) + 1):
                for j in range(abs(y1 - y2) + 1):
                    save_coords((min(x1, x2) + i, min(y1, y2) + j))
        elif (y1 - y2) // (x1 - x2) == 1:
            for i in range(abs(x1 - x2) + 1):
                save_coords((min(x1, x2) + i, min(y1, y2) + i))
        else:
            for i in range(abs(x1 - x2) + 1):
                save_coords((min(x1, x2) + i, max(y1, y2) - i))
            
    overlaps = sum(x > 1 for x in coords.values())
    print(overlaps)
