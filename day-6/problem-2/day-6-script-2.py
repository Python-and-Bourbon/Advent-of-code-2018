from collections import defaultdict
x_low, x_high, y_low, y_high, lines = 500, 0, 500, 0, []
with open('input.txt', 'r') as inp:
    for line in inp.readlines():
        x, y = map(int, line.split(', '))
        x_low, x_high, y_low, y_high = min(x_low, x), max(x_high, x), min(y_low, y), max(y_high, y)
        lines.append((x, y))
distance, safe = lambda x, y: abs(x[0]-y[0])+abs(x[1]-y[1]), 0
for x in range(x_low, x_high+1):
    for y in range(y_low, y_high+1):
        if sum([distance(i, (x, y)) for i in lines]) <= 10000: safe += 1
print(safe)