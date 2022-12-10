with open('input-10.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

# Part 1
x = [1]
for line in lines:
    if line.startswith('noop'):
        x.append(x[-1])
    else:
        v = int(line.split(' ')[1])
        x.append(x[-1])
        x.append(x[-1] + v)

signal_stength = sum([x[i]*(i+1) for i in range(19, 221, 40)])

print(f'Part 1: {signal_stength}')

# Part 2
print('Part 2:')

cycle = 0
for row in range(6):
    crt_output = []
    for col in range(40):
        if abs(x[cycle] - col) <= 1:
            crt_output.append('#')
        else:
            crt_output.append('.')
        cycle += 1
    print(' '.join(crt_output))
