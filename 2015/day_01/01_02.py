with open('2015/day_01/input_01.txt') as input:
    floor = 0
    for i, c in enumerate(input.readline()):
        floor += 1 if c == '(' else -1
        if floor == -1:
            print(i + 1)
            break
