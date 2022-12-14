with open('input-14.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

STARTING_POINT = (500, 0)


def get_initial_occupied_points(lines):
    occupied_points = set()
    for line in lines:
        points = [eval(point) for point in line.split(' -> ')]

        for i in range(1, len(points)):
            p1x, p1y = points[i-1]
            p2x, p2y = points[i]

            delta_x = p2x - p1x
            delta_y = p2y - p1y

            if delta_x > 0:
                for x in range(p1x, p2x + 1):
                    occupied_points.add((x, p1y))
            elif delta_x < 0:
                for x in range(p1x, p2x - 1, -1):
                    occupied_points.add((x, p1y))
            elif delta_y > 0:
                for y in range(p1y, p2y + 1):
                    occupied_points.add((p1x, y))
            elif delta_y < 0:
                for y in range(p1y, p2y - 1, -1):
                    occupied_points.add((p1x, y))

    return occupied_points


def get_next_pos(pos):
    x, y = pos
    yield from [(x, y+1), (x-1, y+1), (x+1, y+1)]

# This runs a little slow (5 sec.), so it needs optimization.
def drop_sand(occupied_points, max_y, part, current_pos=STARTING_POINT):
    while True:
        for next_pos in get_next_pos(current_pos):
            if next_pos not in occupied_points:
                current_pos = next_pos
                break

        if (part == 1 and current_pos[1] == max_y) or (part == 2 and STARTING_POINT in occupied_points):
            return False
        elif (current_pos != next_pos) or (part == 2 and current_pos[1] == max_y - 1):
            occupied_points.add(current_pos)
            return True


# Part 1
occupied_points = get_initial_occupied_points(lines)
max_y = max([point[1] for point in occupied_points])
initial_count = len(occupied_points)

while drop_sand(occupied_points, max_y, part=1):
    pass

print(f'Part 1: {len(occupied_points) - initial_count}')

# Part 2
occupied_points = get_initial_occupied_points(lines)
max_y += 2

while drop_sand(occupied_points, max_y, part=2):
    pass

print(f'Part 2: {len(occupied_points) - initial_count}')
