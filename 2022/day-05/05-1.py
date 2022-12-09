import math
import re

stacks = [ [] for _ in range(9) ]

with open('input.txt') as input:
    # read crates
    while True:
        line = input.readline()
        if line[0].isspace():
            break

        # read characters
        line_length = len(line)
        for i in range(line_length):
            if line[i].isalpha():
                target_stack = math.ceil(i / 4) - 1
                stacks[target_stack].insert(0, line[i]) # insert in front

    # consume empty line
    input.readline()

    # read moves
    while True:
        line = input.readline()
        if line.isspace() or not line:
            break
        move = re.split(' from | to ', line[5:].strip())
        if len(move) <= 1:
            break
        crates_to_move = int(move[0])
        from_stack = int(move[1]) - 1
        to_stack = int(move[2]) - 1
        for crates in range(crates_to_move):
            stacks[to_stack].append(stacks[from_stack].pop())

    # get top crates
    top_crates = ''.join([ s.pop() for s in stacks ])
    print(top_crates)