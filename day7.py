from collections import defaultdict

with open('input-7.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

# Part 1
pathStack = []
dirSizes = defaultdict(int)

for line in lines:
    logEntry = line.split(' ')
    if logEntry[0] == '$':
        if logEntry[1] == 'cd':
            if logEntry[2] == '..':
                pathStack.pop()
            else:
                pathStack.append(logEntry[2])
    elif logEntry[0] != 'dir':
        fileSize = int(logEntry[0])
        for i in range(1, len(pathStack) + 1):
            path = '/'.join(pathStack[:i])
            dirSizes[path] += fileSize

totalSizes = sum([x for x in dirSizes.values() if x <= 100000])
print(f'Part 1: {totalSizes}')

# Part 2
TOTAL_DISK_SIZE = 70000000
REQUIRED_SPACE = 30000000

unusedSpace = TOTAL_DISK_SIZE - dirSizes['/']
minSpaceNeeded = max(0, REQUIRED_SPACE - unusedSpace)

spaceToFree = min([x for x in dirSizes.values() if x >= minSpaceNeeded])

print(f'Part 2: {spaceToFree}')
