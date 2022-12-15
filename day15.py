
# Both parts work, but are slow. Needs optimization.

from re import findall

X_REGEX = 'x=-?[0-9]+'
Y_REGEX = 'y=-?[0-9]+'

with open('input-15.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def get_positions_and_distances(lines):
    distances = set()
    positions = {}
    for line in lines:
        xs, xb = [int(x.split('=')[1]) for x in findall(X_REGEX, line)]
        ys, yb = [int(y.split('=')[1]) for y in findall(Y_REGEX, line)]

        positions[(xs, ys)] = 'S'
        positions[(xb, yb)] = 'B'
        md = manhattan_distance(xs, ys, xb, yb)

        distances.add((xs, ys, md))
    return positions, distances


# Part 1
positions, distances = get_positions_and_distances(lines)
ROW = 2000000
for x, y, md in distances:
    dx = md - abs(y - ROW)
    if dx < 0:
        continue
    for xb in range(x - dx, x + dx + 1):
        if manhattan_distance(x, y, xb, ROW) <= md and (xb, ROW) not in positions:
            positions[(xb, ROW)] = '#'

no_beacon_count = len(
    [pos for (pos, type) in positions.items() if pos[1] == ROW and type == '#'])
print(f'Part 1: {no_beacon_count}')

# Part 2
MIN_COORD = 0
MAX_COORD = 4000000


def is_position_away_from_all_sensors(bx, by, distances):
    for x, y, md in distances:
        if manhattan_distance(x, y, bx, by) <= md:
            return False
    return True


def find_position(distances):
    for x, y, md in distances:
        # Find the point that is md+1 away from all sensors
        for dx in range(0, md+2):
            dy = md + 1 - dx
            for dirx, diry in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                bx = x + (dx*dirx)
                by = y + (dy*diry)
                if MIN_COORD <= bx <= MAX_COORD and MIN_COORD <= by <= MAX_COORD:
                    if is_position_away_from_all_sensors(bx, by, distances):
                        return (bx, by)


_, distances = get_positions_and_distances(lines)
position = find_position(distances)

print(f'Part 2: {position}={position[0]*4000000+position[1]}')
