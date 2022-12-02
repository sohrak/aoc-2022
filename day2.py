# Part 1
with open('input-2.txt', 'r') as f:
    lines = f.readlines()

move_map = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'R',
    'Y': 'P',
    'Z': 'S'
}

move_values = {
    'R': 1,
    'P': 2,
    'S': 3
}

# (me, opponent)
winning_moves = {
    ('R', 'S'),
    ('P', 'R'),
    ('S', 'P')
}

score = 0
for line in lines:
    opponent, me = [move_map[x] for x in line.rstrip('\n').split(' ')]
    score += move_values[me]
    if me == opponent:
        score += 3
    elif (me, opponent) in winning_moves:
        score += 6

print(f'Part 1: {score}')

# Part 2
winning_choice_for_opponent_move = {
    'R': 'P',
    'P': 'S',
    'S': 'R'
}

losing_choice_for_opponent_move = {
    'R': 'S',
    'P': 'R',
    'S': 'P'
}

score = 0
for line in lines:
    opponent, result = line.rstrip('\n').split(' ')
    opponent = move_map[opponent]
    if result == 'Z':
        me = winning_choice_for_opponent_move[opponent]
        score += 6
    elif result == 'Y':
        me = opponent
        score += 3
    else:
        me = losing_choice_for_opponent_move[opponent]
    score += move_values[me]

print(f'Part 2: {score}')
