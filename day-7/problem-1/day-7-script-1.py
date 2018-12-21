with open('input.txt', 'r') as inp: lines = [line.split()[1:8:6] for line in inp.readlines()]
steps = set([line[0] for line in lines] + [line[1] for line in lines])
def next_step(steps, lines): return [step for step in steps if all(b != step for (_, b) in lines)]
while steps:
    readies = sorted(next_step(steps, lines))
    next = readies[0]
    print(next, end='')
    steps.remove(next)
    lines = [(a, b) for (a, b) in lines if a != next]
print()