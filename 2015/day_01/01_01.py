with open('2015/day_01/input_01.txt') as input:
    line = input.readline()
    print(2 * line.count('(') - (len(line)))

    # x = up - down
    # down = total - up
    # x = up - (total - up)
    # x = 2 * up - total