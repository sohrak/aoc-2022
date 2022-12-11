from math import prod

with open('input-11.txt', 'r') as f:
    lines = [line.rstrip('\n').lstrip(' ') for line in f.readlines()]


class Monkey:
    def __init__(self):
        self.items = None
        self.operation = None
        self.test = None
        self.true_monkey = None
        self.false_monkey = None

    def __repr__(self):
        return f'[Items: {self.items}, ' \
            + f'Operation: {self.operation}, ' \
            + f'Test: {self.test}, ' \
            + f'True: {self.true_monkey}, ' \
            + f'False: {self.false_monkey}]'


def get_monkeys(lines):
    MONKEY_LINE = "Monkey "
    ITEMS_LINE = 'Starting items: '
    OPERATION_LINE = 'Operation: new = '
    TEST_LINE = 'Test: divisible by '
    TRUE_LINE = 'If true: throw to monkey '
    FALSE_LINE = 'If false: throw to monkey '

    monkeys = []
    for line in lines:
        if line.startswith(MONKEY_LINE):
            monkeys.append(Monkey())
        elif line.startswith(ITEMS_LINE):
            items = [int(s) for s in line.removeprefix(
                ITEMS_LINE).split(',')]
            monkeys[-1].items = items
        elif line.startswith(OPERATION_LINE):
            monkeys[-1].operation = eval('lambda old: ' +
                                         line.removeprefix(OPERATION_LINE))
        elif line.startswith(TEST_LINE):
            monkeys[-1].test = int(line.removeprefix(TEST_LINE))
        elif line.startswith(TRUE_LINE):
            monkeys[-1].true_monkey = int(line.removeprefix(TRUE_LINE))
        elif line.startswith(FALSE_LINE):
            monkeys[-1].false_monkey = int(line.removeprefix(FALSE_LINE))
    return monkeys


# Part 1
monkeys = get_monkeys(lines)
inspection_counts = [0 for _ in monkeys]
for _ in range(20):
    for i, monkey in enumerate(monkeys):
        for old in monkey.items:
            inspection_counts[i] += 1
            new = monkey.operation(old) // 3
            next_monkey = monkey.true_monkey if new % monkey.test == 0 else monkey.false_monkey
            monkeys[next_monkey].items.append(new)
        monkey.items = []

inspection_counts.sort()
print(f'Part 1: {inspection_counts[-1] * inspection_counts[-2]}')

# Part 2
monkeys = get_monkeys(lines)
lcm = prod([monkey.test for monkey in monkeys])
inspection_counts = [0 for _ in monkeys]
for _ in range(10000):
    for i, monkey in enumerate(monkeys):
        for old in monkey.items:
            inspection_counts[i] += 1
            new = monkey.operation(old) % lcm
            next_monkey = monkey.true_monkey if new % monkey.test == 0 else monkey.false_monkey
            monkeys[next_monkey].items.append(new)
        monkey.items = []

inspection_counts.sort()
print(f'Part 2: {inspection_counts[-1] * inspection_counts[-2]}')
