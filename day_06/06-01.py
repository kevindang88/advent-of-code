with open('day_06/input_06.txt') as input:
    fish = [0] * 9
    for i in map(int, input.readline().split(',')):
        fish[i] += 1

    for _ in range(80):
        spawn = fish[0]
        fish[0] = fish[1]
        fish[1] = fish[2]
        fish[2] = fish[3]
        fish[3] = fish[4]
        fish[4] = fish[5]
        fish[5] = fish[6]
        fish[6] = spawn + fish[7]
        fish[7] = fish[8]
        fish[8] = spawn

    total = sum(fish)
    print(total)