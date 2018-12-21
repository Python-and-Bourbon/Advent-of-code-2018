from collections import defaultdict
x_low, x_high, y_low, y_high, lines = 500, 0, 500, 0, []
with open('input.txt', 'r') as inp:
    for line in inp.readlines():
        x, y = map(int, line.split(', '))
        x_low, x_high, y_low, y_high = min(x_low, x), max(x_high, x), min(y_low, y), max(y_high, y)
        lines.append((x, y))
neighbors, ineligible, distance = defaultdict(int), set(), lambda x, y: abs(x[0]-y[0])+abs(x[1]-y[1])
for x in range(x_low, x_high+1):
    for y in range(y_low, y_high+1):
        d = sorted(map(lambda line: [distance(line, (x, y)), str(line)], lines))
        if x in (x_low, x_high) or y in (y_low, y_high): ineligible.add(d[0][1])
        elif d[0][0] != d[1][0]: neighbors[d[0][1]] += 1
out = 0
for key in neighbors:
    if key not in ineligible: out = max(out, neighbors[key])
print(out)