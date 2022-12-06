def get_rating(list, oxy, index=0):
    list_1, list_0 = [], []
    if len(list) <= 1:
        return list
    else:
        for line in list:
            if line[index] == '1':
                list_1.append(line)
            else:
                list_0.append(line)
        if (len(list_1) >= len(list_0)) == oxy:
            target_list = list_1
        else:
            target_list = list_0
        return get_rating(target_list, oxy, index + 1)

with open('day_03/input_03.txt') as input:
    input_list = input.readlines()

    oxy = int(get_rating(input_list, True)[0], 2)
    co2 = int(get_rating(input_list, False)[0], 2)
    print(oxy * co2)
