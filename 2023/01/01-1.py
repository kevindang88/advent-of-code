import re

sum = 0

with open('input') as file:
    for line in file:
        calibration_value = int(re.search('\\d', line).group() + re.search('\\d', line[::-1]).group())
        print(calibration_value)
        sum = sum + calibration_value

print(sum)