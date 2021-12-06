import re

with open('day_05/input_05.txt') as input:
    coords = []
    overlaps = set()
    for line in input:
        x1, y1, x2, y2 = re.split(',| -> ', line.strip())
        