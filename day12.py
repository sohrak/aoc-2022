from collections import deque

with open('input-12.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def get_value(c):
    if c == 'S':
        return ord('a')
    elif c == 'E':
        return ord('z')
    else:
        return ord(c)


def can_move_part1(start, end):
    return get_value(end) - get_value(start) <= 1


def can_move_part2(start, end):
    return get_value(start) - get_value(end) <= 1


def parse_graph(lines, start_char, end_char, can_move):
    successor_map = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == start_char:
                start = (i, j)
            if c == end_char:
                end = (i, j)
            edges = []
            if i > 0 and can_move(c, lines[i-1][j]):
                # up
                edges.append((i-1, j))
            if i < len(lines) - 1 and can_move(c, lines[i+1][j]):
                # down
                edges.append((i+1, j))
            if j > 0 and can_move(c, lines[i][j-1]):
                # left
                edges.append((i, j-1))
            if j < len(line) - 1 and can_move(c, lines[i][j+1]):
                # right
                edges.append((i, j+1))
            successor_map[(i, j)] = edges
    return successor_map, start, end


# BFS based on AIMA 4e
def bfs(successor_map, start, is_goal):
    if is_goal(start):
        return 0

    frontier = deque()
    frontier.append((0, start))
    reached = set()

    while frontier:
        move_count, node = frontier.popleft()
        if node in reached:
            continue
        reached.add(node)
        for child in successor_map[node]:
            if is_goal(child):
                return move_count + 1
            frontier.append((move_count + 1, child))

    return -1


# Part 1
successor_map, start, end = parse_graph(lines, 'S', 'E', can_move_part1)
move_count = bfs(successor_map, start, lambda x: x == end)

print(f'Part 1: {move_count}')

# Part 2 - search backwards
successor_map, start, end = parse_graph(lines, 'E', 'S', can_move_part2)
move_count = bfs(successor_map, start, lambda x: lines[x[0]][x[1]] == 'a')

print(f'Part 2: {move_count}')
