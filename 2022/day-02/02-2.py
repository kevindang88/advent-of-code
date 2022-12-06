with open('input.txt') as input_file:
    lines = input_file.readlines()

shapes = {
    'A': 1, 'B': 2, 'C': 3
}

outcomes = {
    'X': 0, 'Y': 3, 'Z': 6
}

def is_odd(n):
    return n % 2 != 0

def is_pos(n):
    return n > 0

score = 0

for line in lines:
    opp_shape, outcome = line.strip().split(' ')
    opp_score = shapes.get(opp_shape)
    score += outcomes.get(outcome)
    if outcome == 'Y':   # draw
        score += opp_score
    elif outcome == 'X': # lose
        score += ((opp_score - 2) % 3) + 1
    else:                # win
        score += (opp_score % 3) + 1

print(score)
