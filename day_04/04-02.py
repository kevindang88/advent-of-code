with open('day_04/input_04.txt') as input:
    draw_numbers = input.readline().split(',')
    marked = [[0 for i in range(10)] for j in range(100)]

    # create 1-D array of all boards
    boards = []
    for line in input:
        for i in line.split():
            boards.append(int(i))

    # for debugging
    # def print_board(b):
    #     for r in range(0, 5):
    #         for c in range(0, 5):
    #             print(boards[(b*25)+(r*5)+c], end=' ')
    #         print('\n')

    # create map of all numbers on all boards
    num_map = [[] for i in range(100)]
    for index, value in enumerate(boards):
        b = int(index / 25)
        r = int((index % 25) / 5)
        c = index % 5
        num_map[value].append([b, r, c])

    # draw numbers, check for bingo, update latest winning b coordinate
    has_bingo = [False for i in range(100)]
    for number in draw_numbers:
        for coords in num_map[int(number)]:
            b, r, c = coords
            if not has_bingo[int(b)]:
                index = (25 * b) + (5 * r) + c
                boards[index] = 'x'
                marked[b][r] += 1
                marked[b][c + 5] += 1
                if marked[b][r] == 5 or marked[b][c + 5] == 5: # bingo
                    has_bingo[int(b)] = True
                    last_bingo_b = b
                    last_bingo_number = number    

    # calculate score of last winning board
    score = 0
    for n in range(last_bingo_b * 25, (last_bingo_b + 1) *25):
        if boards[int(n)] != 'x':
            score += boards[int(n)]
    score *= int(last_bingo_number)
    print('final score: ' + str(score))
