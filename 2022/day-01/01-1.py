with open('input.txt') as input_file:
    lines = input_file.readlines()

max_calories = 0
sum = 0

for line in lines:
    if line.isspace():
        if sum > max_calories:
            max_calories = sum
        sum = 0
    else:
        sum += int(line)

print(max_calories)
