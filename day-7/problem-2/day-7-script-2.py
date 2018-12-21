with open('input.txt', 'r') as inp: lines = [line.split()[1:8:6] for line in inp.readlines()]
steps, vals = set([line[0] for line in lines] + [line[1] for line in lines]), lambda x: 60 + ord(x) - ord('A')
def next_step(steps, lines): return [step for step in steps if all(b != step for (_, b) in lines)]
workers, wip, time_used = [0 for _ in range(5)], [None for _ in range(5)], 0
while steps or any(i > 0 for i in workers):
    readies, time_used = sorted(next_step(steps, lines))[::-1], time_used + 1
    for i in range(5):
        workers[i] = max(0, workers[i]-1)
        if workers[i] == 0:
            if wip[i] is not None: lines = [(a, b) for (a, b) in lines if a != wip[i]]
            if readies:
                wip[i] = readies.pop()
                workers[i] = vals(wip[i])
                steps.remove(wip[i])
print(time_used)