with open('input-5.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def getInitialStacks(stackLines):
    STACK_VALUE_OFFSET = 1
    STACK_WIDTH = 4
    stackCount = (len(stackLines[0]) + 1) // STACK_WIDTH
    stacks = [list() for _ in range(stackCount)]
    for line in stackLines:
        if line == '':
            break
        for i, c in enumerate(line):
            if c.isalpha():
                index = (i - STACK_VALUE_OFFSET) // STACK_WIDTH
                stacks[index].insert(0, c)
    return stacks

# Part 1
stacks = getInitialStacks(lines)
for line in lines:
    if line.startswith('move'):
        count, src, dest = [int(s) for s in line.replace('move ', '').replace('from ', '').replace('to ', '').split(' ')]
        for _ in range(count):
            stacks[dest-1].append(stacks[src-1].pop())

print(f'Part 1: {"".join([stack[-1] for stack in stacks])}')

# Part 2
stacks = getInitialStacks(lines)
for line in lines:
    if line.startswith('move'):
        count, src, dest = [int(s) for s in line.replace('move ', '').replace('from ', '').replace('to ', '').split(' ')]
        stacks[dest-1].extend(stacks[src-1][-count:])
        del stacks[src-1][-count:]

print(f'Part 2: {"".join([stack[-1] for stack in stacks])}')
