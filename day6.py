with open('input-6.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

def getUniqueSequenceCharCount(packet, sequenceLength):
    for i in range(sequenceLength, len(packet)):
        if len(set(packet[i-sequenceLength:i])) == sequenceLength:
            return i

# Part 1
print(f'Part 1: {getUniqueSequenceCharCount(lines[0], 4)}')

# Part 2
print(f'Part 2: {getUniqueSequenceCharCount(lines[0], 14)}')
