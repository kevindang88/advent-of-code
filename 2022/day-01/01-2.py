from collections import deque

with open('input.txt') as input_file:
    lines = input_file.readlines()

top_three = deque([0, 0, 0], 3)

cal_sum = 0

for line in lines:
    if line.isspace():
        if cal_sum > top_three[0]:
            top_three.appendleft(cal_sum)
        elif cal_sum > top_three[1]:
            top_three.pop()
            top_three.insert(1, cal_sum)
        elif cal_sum > top_three[2]:
            top_three.append(cal_sum)
        cal_sum = 0
    else:
        cal_sum += int(line)

print(sum(top_three))
