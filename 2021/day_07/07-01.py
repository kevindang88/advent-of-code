with open('day_07/input_07.txt') as input:
    positions = list(map(int, input.readline().split(',')))
    positions.sort()
    median = positions[len(positions) // 2]
    fuel_cost = sum(abs(x - median) for x in positions)
    print(fuel_cost)