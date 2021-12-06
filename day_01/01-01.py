with open('day_01/input.txt') as input:
    count = 0
    prev = input.readline()
    for line in input:
        if int(line) > int(prev):
            count += 1
        prev = line
    print(count)