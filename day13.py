from functools import cmp_to_key

with open('input-13.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


# Define a standard comparator function, returning -1, 0, or 1.
def compare_values(left, right):
    if type(left) is int and type(right) is int:
        if left < right:
            return -1
        elif left > right:
            return 1
    else:
        if type(left) is not list:
            left = [left]
        if type(right) is not list:
            right = [right]

        for i in range(max(len(left), len(right))):
            if i >= len(left):
                return -1
            elif i >= len(right):
                return 1
            else:
                compare_output = compare_values(left[i], right[i])
                if compare_output != 0:
                    return compare_output
    return 0


# Part 1
correct_order_sum = 0
packet_index = 0
for i in range(0, len(lines), 3):
    packet_index += 1

    packet1 = eval(lines[i])
    packet2 = eval(lines[i+1])

    if compare_values(packet1, packet2) == -1:
        correct_order_sum += packet_index

print(f'Part 1: {correct_order_sum}')

# Part 2
packets = [eval(line) for line in lines if line]
packets.extend([[[2]], [[6]]])

packets.sort(key=cmp_to_key(compare_values))
decoder_key = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

print(f'Part 2: {decoder_key}')
