with open('input-4.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def rangeStrToSet(s):
    low, high = [int(x) for x in s.split('-')]
    return set(range(low, high + 1))


# Part 1
count = 0
for line in lines:
    range1, range2 = line.split(',')
    set1 = rangeStrToSet(range1)
    set2 = rangeStrToSet(range2)
    if set1.issubset(set2) or set2.issubset(set1):
        count += 1

print(f'Part 1: {count}')

# Part 2
count = 0
for line in lines:
    range1, range2 = line.split(',')
    set1 = rangeStrToSet(range1)
    set2 = rangeStrToSet(range2)
    if set1.intersection(set2):
        count += 1

print(f'Part 2: {count}')
