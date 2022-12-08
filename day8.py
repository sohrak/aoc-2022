with open('input-8.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

grid = []
for line in lines:
    grid.append([int(c) for c in line])

# Part 1
visibleCount = len(grid[0]) + len(grid[-1])
for i in range(1, len(grid) - 1):
    visibleCount += 2
    for j in range(1, len(grid[i]) - 1):
        value = grid[i][j]
        maxUp = max([grid[x][j] for x in range(0, i)])
        maxDown = max([grid[x][j] for x in range(i+1, len(grid))])
        maxLeft = max(grid[i][:j])
        maxRight = max(grid[i][j+1:])
        if value > min(maxUp, maxDown, maxLeft, maxRight):
            visibleCount += 1

print(f'Part 1: {visibleCount}')

# Part 2


def calcScore(tree, otherTrees):
    score = 0
    for otherTree in otherTrees:
        score += 1
        if tree <= otherTree:
            break
    return score


bestScore = 0
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        value = grid[i][j]
        upScore = calcScore(value, [grid[x][j] for x in reversed(range(0, i))])
        downScore = calcScore(value, [grid[x][j]
                              for x in range(i+1, len(grid))])
        leftScore = calcScore(value, reversed(grid[i][:j]))
        rightScore = calcScore(value, grid[i][j+1:])
        totalScore = upScore * downScore * leftScore * rightScore
        bestScore = max(bestScore, totalScore)

print(f'Part 2: {bestScore}')
