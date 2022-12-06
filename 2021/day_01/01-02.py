with open('day_01/input.txt') as input:
    count = 0
    a = int(input.readline())
    b = int(input.readline())
    c = int(input.readline())
    prev3 = a + b + c
    for line in input:
        if line != '' and b + c + int(line) > prev3:
            count += 1
        a = b
        b = c
        c = int(line)
        prev3 = a + b + c
    print(count)
    