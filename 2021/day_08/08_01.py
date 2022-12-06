with open ('day_08/input_08.txt') as input:
    count = 0

    for line in input:
        values = line.strip().split('|')[1].split(' ')
        for v in values:
            if len(v) in [2, 3, 4, 7]:
                count += 1

    print(count)
        
# digit :   segments
# 1     :   2
# 4     :   4
# 7     :   3
# 8     :   7
