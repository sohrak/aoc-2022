from math import sqrt

with open('input-9.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def sign(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1


# Part 1
h_pos_x = 0
h_pos_y = 0

t_pos_x = 0
t_pos_y = 0

visited_pos = {(0, 0)}

for line in lines:
    direction, steps = line.split(' ')

    for _ in range(int(steps)):
        if direction == 'U':
            h_pos_y += 1
        elif direction == 'D':
            h_pos_y -= 1
        elif direction == 'L':
            h_pos_x -= 1
        elif direction == 'R':
            h_pos_x += 1

        delta_x = h_pos_x - t_pos_x
        delta_y = h_pos_y - t_pos_y

        x_not_touching = abs(delta_x) > 1
        y_not_touching = abs(delta_y) > 1

        if x_not_touching or y_not_touching:
            t_pos_x += sign(delta_x)
            t_pos_y += sign(delta_y)

        visited_pos.add((t_pos_x, t_pos_y))

print(f'Part 1: {len(visited_pos)}')

# Part 2
positions = [(0, 0) for _ in range(10)]
visited_pos = {(0, 0)}

for line in lines:
    direction, steps = line.split(' ')

    for _ in range(int(steps)):
        h_pos_x, h_pos_y = positions[0]

        if direction == 'U':
            h_pos_y += 1
        elif direction == 'D':
            h_pos_y -= 1
        elif direction == 'L':
            h_pos_x -= 1
        elif direction == 'R':
            h_pos_x += 1

        positions[0] = (h_pos_x, h_pos_y)

        for i in range(1, len(positions)):
            prev_pos_x, prev_pos_y = positions[i-1]
            curr_pos_x, curr_pos_y = positions[i]

            delta_x = prev_pos_x - curr_pos_x
            delta_y = prev_pos_y - curr_pos_y

            x_not_touching = abs(delta_x) > 1
            y_not_touching = abs(delta_y) > 1

            if x_not_touching or y_not_touching:
                positions[i] = (curr_pos_x + sign(delta_x),
                                curr_pos_y + sign(delta_y))

        visited_pos.add(positions[-1])

print(f'Part 2: {len(visited_pos)}')
