from collections import defaultdict
with open('input.txt', 'r') as inp: lines = sorted([line.rstrip('\n') for line in inp.readlines()])
minute, guard_id, m, n, guard_sleep, guard_minute = lambda x: int(x[15:17]), lambda x: int(x.split(' ')[3][1:]), 0, 0, defaultdict(int), defaultdict(int)
for i in lines:
    if 'Guard' in i: current_guard = guard_id(i)
    elif 'falls' in i: sleep = minute(i)
    else: 
        guard_sleep[current_guard] += minute(i) - sleep
        if guard_sleep[current_guard] > m: m, best_guard = guard_sleep[current_guard], current_guard
for i in lines:
    if 'Guard' in i: current_guard, sleep = guard_id(i), False
    if current_guard == best_guard:
        if 'falls' in i: sleep = minute(i)
        elif 'wakes' in i:
            for time in range(sleep, minute(i)): 
                guard_minute[time] += 1
                if guard_minute[time] > n: n, best_minute = guard_minute[time], time
print(best_guard * best_minute)