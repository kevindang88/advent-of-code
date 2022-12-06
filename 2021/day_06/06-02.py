with open('day_06/input_06.txt') as input:
    fish = [0] * 9
    for i in map(int, input.readline().split(',')):
        fish[i] += 1

    for _ in range(256):
        spawn = fish[0]
        for i in range(8):
            fish[i] = fish[i + 1]
        fish[6] += spawn
        fish[8] = spawn
        
    total = sum(fish)
    print(total)