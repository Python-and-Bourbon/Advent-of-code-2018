from collections import defaultdict
with open('input.txt', 'r') as inp: lines = sorted([line.rstrip('\n') for line in inp.readlines()])
minute, guard_id, m, guard_minute = lambda x: int(x[15:17]), lambda x: int(x.split(' ')[3][1:]), 0, defaultdict(int)
for i in lines:
    if 'Guard' in i: current_guard = guard_id(i)
    elif 'falls' in i: sleep = minute(i)
    else:
        for time in range(sleep, minute(i)): 
                guard_minute[(current_guard, time)] += 1
                if guard_minute[(current_guard, time)] > m: m, best = guard_minute[(current_guard, time)], (current_guard, time)
print(best[0] * best[1])