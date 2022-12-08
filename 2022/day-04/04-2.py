import re

overlaps = 0

with open('input.txt') as input:
    while True:
        line = input.readline().strip()
        if not line:
            break
        sections = list(map(lambda s: int(s), re.split(',|-', line)))
        if ((sections[0] <= sections[2] and sections[1] >= sections[2])
            or (sections[2] <= sections[0] and sections[3] >= sections[0])):
            overlaps += 1

print(overlaps)
