import re

fully_contained = 0

with open('input.txt') as input:
    while True:
        line = input.readline().strip()
        if not line:
            break
        sections = list(map(lambda s: int(s), re.split(',|-', line)))
        if ((sections[0] <= sections[2] and sections[1] >= sections[3])
                or (sections[0] >= sections[2] and sections[1] <= sections[3])):
            fully_contained += 1

print(fully_contained)