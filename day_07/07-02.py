with open('day_07/example_input.txt') as input:
    positions = list(map(int, input.readline().split(',')))

    mean_floor = ((sum(positions) / len(positions))).__floor__()

    fuel_cost_floor = 0
    for p in positions:
        fuel_cost_floor += sum([x for x in range(abs(mean_floor - p) + 1)])

    print(fuel_cost_floor)