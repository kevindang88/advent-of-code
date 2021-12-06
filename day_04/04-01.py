with open('day_04/input_04.txt') as input:
    draw_numbers = input.readline().split(',')
    marked = [[0 for i in range(10)] for j in range(100)]

    # create 1-D array of all boards
    boards = []
    for line in input:
        for i in line.split():
            boards.append(int(i))

    # create map of all numbers on all boards
    num_map = [[] for i in range(100)]
    for index, value in enumerate(boards):
        b = int(index / 25)
        r = int((index % 25) / 5)
        c = index % 5
        num_map[value].append([b, r, c])

    # draw numbers, check for bingo, calculate score
    for number in draw_numbers:
        for coords in num_map[int(number)]:
            b, r, c = coords
            index = (25 * b) + (5 * r) + c
            boards[index] = 'x'
            marked[b][r] += 1
            marked[b][c + 5] += 1
            if marked[b][r] == 5 or marked[b][c + 5] == 5: # bingo
                score = 0
                for n in range(b * 25, (b + 1) *25):
                    if boards[int(n)] != 'x':
                        score += boards[int(n)]
                score *= int(number)
                print(score)
                exit()
