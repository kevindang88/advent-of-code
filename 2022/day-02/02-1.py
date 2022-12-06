with open('input.txt') as input_file:
    lines = input_file.readlines()

shapes = {
    'A': 1, 'B': 2, 'C': 3,
    'X': 1, 'Y': 2, 'Z': 3
}

points = {
    'win': 6, 'draw': 3, 'lose': 0
}

def is_odd(n):
    return n % 2 != 0

def is_pos(n):
    return n > 0

score = 0

for line in lines:
    opp_shape, my_shape = map(lambda s: shapes.get(s), line.strip().split(' '))
    result = my_shape - opp_shape
    if result == 0:
        score += points.get('draw')
    elif (is_pos(result) and is_odd(result)) or (not is_odd(result) and not is_pos(result)):
        score += points.get('win')
    else:
        score += points.get('lose')
    score += my_shape

print(score)
