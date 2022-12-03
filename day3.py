# Part 1
with open('input-3.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

lower_priority_start = 1
upper_priority_start = 27

lower_priority_base = ord('a')
upper_priority_base = ord('A')

total_priority = 0
for line in lines:
    mid = len(line) // 2
    value = set(line[:mid]).intersection(set(line[mid:])).pop()

    if value.islower():
        priority = ord(value) - lower_priority_base + lower_priority_start
    else:
        priority = ord(value) - upper_priority_base + upper_priority_start

    total_priority += priority

print(f'Part 1: {total_priority}')

# Part 2
total_priority = 0
for i in range(0, len(lines), 3):
    line1 = lines[i]
    line2 = lines[i+1]
    line3 = lines[i+2]

    value = set(line1).intersection(set(line2)).intersection(set(line3)).pop()

    if value.islower():
        priority = ord(value) - lower_priority_base + lower_priority_start
    else:
        priority = ord(value) - upper_priority_base + upper_priority_start

    total_priority += priority

print(f'Part 2: {total_priority}')
