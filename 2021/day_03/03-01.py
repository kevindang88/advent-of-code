with open('day_03/input_03.txt') as input:
    bit_counts = [int(i) for i in input.readline().strip()]
    line_count = 1

    for line in input:
        line_count += 1
        for i in range(0, len(line) - 1):
            bit_counts[i] += int(line[i])

    gamma = []
    epsilon = []
    for i in bit_counts:
        if int(i) > line_count / 2:
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')
    gamma = ''.join(gamma)
    epsilon = ''.join(epsilon)

    print(int(gamma, base=2) * int(epsilon, base=2))
