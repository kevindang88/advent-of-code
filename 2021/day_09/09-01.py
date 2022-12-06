with open('day_09/input_09.txt') as input:
    heightmap = []
    for line in input:
        heightmap.append([int(x) for x in line.strip()])

    print(heightmap)

    def sum_adjacent(heightmap, i, j):
        

    for i in range(len(heightmap[0])):
        for j in range(len(heightmap)):
